#!/usr/bin/env python3
"""Build knowledge star graph from Obsidian vault and workspace markdown files."""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[3]  # workspace root
OUTPUT = WORKSPACE / "memory" / "ontology" / "knowledge_graph.json"

# Directories to scan for markdown files
SCAN_DIRS = [
    WORKSPACE,
    WORKSPACE / ".." / "ObsidianVault",  # Obsidian vault
]

# Patterns
TAG_RE = re.compile(r'(?<!\w)#([A-Za-z\u4e00-\u9fff\u3400-\u4dbf][\w\u4e00-\u9fff\u3400-\u4dbf-]*)')
WIKILINK_RE = re.compile(r'\[\[([^\]|#]+?)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')

# Directories/files to skip
SKIP = {'.git', 'node_modules', '.venv', '__pycache__', '.obsidian', '.trash'}
SKIP_FILES = {'knowledge_graph.json'}


def file_id(filepath: Path, base: Path) -> str:
    """Generate a stable node ID from a file path."""
    rel = filepath.relative_to(base)
    stem = rel.stem
    # For files in subdirs, use just the stem (matches existing convention)
    return stem


def scan_files():
    """Find all markdown files across scan directories."""
    md_files = []
    seen_paths = set()

    for scan_dir in SCAN_DIRS:
        scan_dir = scan_dir.resolve()
        if not scan_dir.exists():
            continue
        for root, dirs, files in os.walk(scan_dir):
            # Prune skipped dirs
            dirs[:] = [d for d in dirs if d not in SKIP]
            for fname in files:
                if not fname.endswith('.md'):
                    continue
                if fname in SKIP_FILES:
                    continue
                full = Path(root) / fname
                try:
                    full_resolved = full.resolve()
                except OSError:
                    continue
                if full_resolved in seen_paths:
                    continue
                seen_paths.add(full_resolved)
                md_files.append((full, scan_dir))

    return md_files


def extract_metadata(content: str):
    """Extract tags and wikilinks from markdown content."""
    # Remove code blocks
    content_clean = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    content_clean = re.sub(r'`[^`]*`', '', content_clean)

    tags = set(TAG_RE.findall(content_clean))
    wikilinks = set(WIKILINK_RE.findall(content_clean))

    return tags, wikilinks


def build_graph():
    """Build the knowledge star graph."""
    nodes = set()
    edges = []
    tags_map = {}   # tag_name -> [file_ids]
    files_map = {}  # rel_path -> {id, path, type}
    wikilink_set = set()
    edge_set = set()

    md_files = scan_files()
    total_files = len(md_files)

    for filepath, base_dir in md_files:
        fid = file_id(filepath, base_dir)
        try:
            rel_path = str(filepath.relative_to(WORKSPACE))
        except ValueError:
            rel_path = str(filepath.relative_to(base_dir))

        # Add file node
        nodes.add(('file', fid))
        files_map[rel_path] = {"id": fid, "path": rel_path, "type": "file"}

        # Read content
        try:
            content = filepath.read_text(encoding='utf-8', errors='replace')
        except (OSError, UnicodeDecodeError):
            continue

        tags, wikilinks = extract_metadata(content)

        # Process tags
        for tag in tags:
            tag_node_id = f"#{tag}"
            nodes.add(('tag', tag_node_id))
            edge_key = (fid, tag_node_id, 'tag')
            if edge_key not in edge_set:
                edge_set.add(edge_key)
                edges.append({"source": fid, "target": tag_node_id, "type": "tag"})
            tags_map.setdefault(tag, [])
            if fid not in tags_map[tag]:
                tags_map[tag].append(fid)

        # Process wikilinks
        for link in wikilinks:
            link_clean = link.strip()
            if not link_clean:
                continue
            # Determine if it's a concept or file reference
            if link_clean.startswith('reply_to'):
                target_id = link_clean
                nodes.add(('concept', target_id))
            else:
                target_id = link_clean
                # Don't add as node yet - might be external
                nodes.add(('concept', target_id))

            wikilink_set.add((fid, target_id))
            edge_key = (fid, target_id, 'wikilink')
            if edge_key not in edge_set:
                edge_set.add(edge_key)
                edges.append({"source": fid, "target": target_id, "type": "wikilink"})

    # Build final node list
    node_list = []
    seen_node_ids = set()
    for ntype, nid in sorted(nodes, key=lambda x: (x[0], x[1])):
        if nid not in seen_node_ids:
            seen_node_ids.add(nid)
            node_list.append({"id": nid, "type": ntype})

    # Count unique tags (exclude color hex codes)
    real_tags = {t for t in tags_map if not re.match(r'^[0-9a-fA-F]{6}$', t)}

    graph = {
        "meta": {
            "generated": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "total_files_scanned": total_files,
            "total_nodes": len(node_list),
            "total_edges": len(edges),
            "total_tags": len(real_tags),
            "total_wikilinks": len(wikilink_set)
        },
        "nodes": node_list,
        "edges": edges,
        "tags": {k: sorted(v) for k, v in sorted(tags_map.items())},
        "files": dict(sorted(files_map.items()))
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"✅ 知识星图构建完成")
    print(f"   节点: {len(node_list)}")
    print(f"   关联: {len(edges)}")
    print(f"   标签: {len(real_tags)}")
    print(f"   文件: {total_files}")
    print(f"   输出: {OUTPUT}")


if __name__ == '__main__':
    build_graph()

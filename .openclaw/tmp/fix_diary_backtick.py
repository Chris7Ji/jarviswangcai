with open('/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai/js/diary.js', 'rb') as f:
    content = f.read()

# Find the bug: content close for 20260514
# Should be </p>`, (backtick+comma) but it's </p>', (single quote+comma)
idx = content.find(b"</p>',\n        excerpt:")
print(f"Bug found at byte offset: {idx}")
print(f"Context: {content[idx-10:idx+60]}")

# Fix: replace the single quote (0x27) with backtick (0x60)
if idx > 0:
    # The pattern is ...</p>'  ,\n...
    # We want ...</p>`  ,\n...
    # Single quote is at idx+4 (after </p>)
    print(f"Char at idx+4: {hex(content[idx+4])} = {chr(content[idx+4])}")
    
    # Build fixed content
    fixed = content[:idx+4] + b'\x60' + content[idx+5:]
    
    # Verify
    verify_idx = fixed.find(b"</p>'")
    if verify_idx >= 0:
        print(f"⚠️ Still has single quote at {verify_idx}")
    else:
        print("✅ Single quote replaced")
    
    verify_backtick = fixed.find(b"</p>`")
    if verify_backtick >= 0:
        print(f"✅ Backtick found at {verify_backtick}")
    
    # Write fixed file
    with open('/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai/js/diary.js', 'wb') as f:
        f.write(fixed)
    print("✅ File written successfully")

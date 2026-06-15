const fs = require('fs');
const code = fs.readFileSync('/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai/js/diary.js', 'utf8');
const lines = code.split('\n');

// Check for unclosed template literals
let inTemplate = false;
let templateStart = -1;
let inString = false;
let stringChar = '';
let braceCount = 0;

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  for (let c = 0; c < line.length; c++) {
    const ch = line[c];
    // Skip escaped chars
    if (c > 0 && line[c-1] === '\\') continue;
    
    if (inTemplate) {
      if (ch === '`') {
        inTemplate = false;
        templateStart = -1;
      }
    } else if (inString) {
      if (ch === stringChar) {
        inString = false;
      }
    } else {
      if (ch === '"' || ch === "'" || ch === '`') {
        inString = true;
        stringChar = ch;
        if (ch === '`') {
          inTemplate = true;
          templateStart = i + 1;
        }
      }
    }
  }
  // Also count braces outside strings
}

if (inTemplate) {
  console.log('⚠️ UNCLOSED TEMPLATE LITERAL starting around line', templateStart);
} else {
  console.log('✅ Template literals all closed');
}

// Check for "//" misinterpretation - look for division issues
// In JS, `//` in expression context starts a regex
// Let's look for suspicious lines
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  const trimmed = line.trim();
  // Find cases where // might be misinterpreted
  if (trimmed.includes('//') && !trimmed.startsWith('//') && !trimmed.startsWith('*')) {
    // Could be division then regex or comment
  }
}

// Try a different parse approach: check for all `id: '20260` entries to ensure array is well-formed
const idMatches = code.match(/id:\s*'2026/g);
console.log('Found', idMatches ? idMatches.length : 0, 'date references');

// Check the trailing part of the file
const last100Lines = lines.slice(-100);
console.log('\n--- Last 5 lines ---');
for (let i = Math.max(0, lines.length - 5); i < lines.length; i++) {
  console.log(lines[i]);
}

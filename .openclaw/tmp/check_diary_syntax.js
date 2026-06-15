const fs = require('fs');
const code = fs.readFileSync('/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai/js/diary.js', 'utf8');

// Check for placeholder comments that look like unescaped regex
const lines = code.split('\n');

// Find lines with potential issues
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  // Check for unescaped forward slashes that could cause regex parsing
  if (line.includes('//') && !line.trim().startsWith('//')) {
    // Find '//' that is NOT in a string
    // This is tricky, let's just look for any line with // that might be misinterpreted
  }
}

// Better approach: try Function constructor and catch with line info
try {
  new Function(code);
  console.log('SYNTAX_OK');
} catch(e) {
  console.log('SYNTAX_ERROR');
  console.log(e.message);
  // Extract line number from error message
  const match = e.message.match(/line (\d+)/i);
  if (match) {
    const ln = parseInt(match[1]);
    for (let i = Math.max(0, ln - 3); i < Math.min(lines.length, ln + 2); i++) {
      console.log(`${i + 1}: ${lines[i]}`);
    }
  } else {
    // Show last few lines
    const start = Math.max(0, lines.length - 100);
    for (let i = start; i < lines.length; i++) {
      console.log(`${i + 1}: ${lines[i]}`);
    }
  }
}

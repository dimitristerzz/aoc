import fs from 'fs';
import path from 'path';

function readFolder(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const result = [];

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      result.push(...readFolder(fullPath)); // recurse
    } else if (entry.isFile() && entry.name.endsWith('.py')) {
      result.push({
        name: entry.name,
        content: fs.readFileSync(fullPath, 'utf-8'),
        folder: path.basename(dir) // year folder
      });
    }
  }

  return result;
}

export function getSolutions() {
  const solutionsDir = path.join(process.cwd(), 'solutions');
  if (!fs.existsSync(solutionsDir)) return [];
  return readFolder(solutionsDir);
}
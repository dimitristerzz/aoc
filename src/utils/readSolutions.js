import fs from 'fs';
import path from 'path';


export function getSolutions() {
  // Absolute path to src/solutions
  const solutionsDir = path.join(process.cwd(), 'src', 'solutions');

  if (!fs.existsSync(solutionsDir)) {
    console.error('Directory not found:', solutionsDir);
    return [];
  }

  const files = fs.readdirSync(solutionsDir).filter(f => f.endsWith('.py'));

  return files.map((file) => ({
    name: file,
    content: fs.readFileSync(path.join(solutionsDir, file), 'utf-8'),
  }));
}
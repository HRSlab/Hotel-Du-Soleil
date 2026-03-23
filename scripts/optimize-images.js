import sharp from 'sharp';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const IGNORE_DIRS = ['.DS_Store', 'node_modules', '.svelte-kit'];
const IMAGE_EXTS = ['.png', '.jpg', '.jpeg', '.tiff', '.webp'];

const staticDir = path.resolve(__dirname, '../static/imgs');

async function optimizeImages(directory) {
  const files = fs.readdirSync(directory);

  for (const file of files) {
    const fullPath = path.join(directory, file);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      if (!IGNORE_DIRS.includes(file)) {
        await optimizeImages(fullPath);
      }
      continue;
    }

    const ext = path.extname(file).toLowerCase();
    if (IMAGE_EXTS.includes(ext)) {
      if (ext === '.webp') {
        console.log(`Skipping ${file} (Already WebP)`);
        continue;
      }
      const outputName = file.replace(ext, '.webp');
      const outputPath = path.join(directory, outputName);

      // Skip if output exists and is newer than source (unless we want to force re-generation)
      if (fs.existsSync(outputPath) && ext !== '.webp') {
        const sourceStat = fs.statSync(fullPath);
        const outputStat = fs.statSync(outputPath);
        if (outputStat.mtime > sourceStat.mtime) {
          console.log(`Skipping ${file} (WebP already up to date)`);
          continue;
        }
      }

      try {
        console.log(`Optimizing ${file} -> ${outputName}`);
        await sharp(fullPath)
          .webp({ quality: 80, effort: 6 })
          .toFile(outputPath);
      } catch (err) {
        console.error(`Error optimizing ${file}:`, err);
      }
    }
  }
}

console.log('Starting Image Optimization...');
optimizeImages(staticDir).then(() => {
  console.log('Image Optimization Complete!');
}).catch(err => {
  console.error('Optimization failed:', err);
});

from PIL import Image
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1]

# Patterns to convert
patterns = ['*.jpg', '*.jpeg', '_X1A*.jpg']

converted = []
skipped = []

for pattern in patterns:
    for p in SRC_DIR.rglob(pattern):
        webp_path = p.with_suffix('.webp')
        if webp_path.exists():
            skipped.append(str(p))
            continue
        try:
            img = Image.open(p).convert('RGB')
            img.save(webp_path, 'WEBP', quality=70, method=6)
            converted.append((str(p), str(webp_path), p.stat().st_size, webp_path.stat().st_size))
        except Exception as e:
            print(f"Failed to convert {p}: {e}")

# Summary
print(f"Converted {len(converted)} files, skipped {len(skipped)} already-existing webp files.")
for orig, webp, orig_size, new_size in converted:
    print(f"{orig} -> {webp}: {orig_size//1024}KB -> {new_size//1024}KB")

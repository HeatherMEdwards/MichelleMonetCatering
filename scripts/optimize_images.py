#!/usr/bin/env python3
"""
Optimize images in img/ for web: resize to display size and compress.
- Gallery images: max 900px (covers 300px at 3x), JPEG quality 85.
- Hero: skipped (often JPEG-in-PNG; optimizing can increase size).
Overwrites files in place. Run from repo root: python3 scripts/optimize_images.py
Requires: pip install Pillow
"""
from PIL import Image
import os

# img/ is at project root, one level up from this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
IMG_DIR = os.path.join(PROJECT_ROOT, "img")

GALLERY_MAX = 900   # longest side; gallery displays at 300px height
HERO_MAX_WIDTH = 1200
JPEG_QUALITY = 85


def resize_to_max(img, max_size):
    """Resize so longest side is at most max_size; preserve aspect ratio."""
    w, h = img.size
    if w <= max_size and h <= max_size:
        return img
    if w >= h:
        new_w = max_size
        new_h = int(h * max_size / w)
    else:
        new_h = max_size
        new_w = int(w * max_size / h)
    return img.resize((new_w, new_h), Image.Resampling.LANCZOS)


def optimize_jpeg(path):
    """Resize and recompress JPEG; strip EXIF."""
    with Image.open(path) as img:
        img = img.convert("RGB")
        img = resize_to_max(img, GALLERY_MAX)
        img.save(path, "JPEG", quality=JPEG_QUALITY, optimize=True)
    return path


def optimize_hero(path):
    """Resize hero to max width; save as PNG (keeps same filename for links)."""
    with Image.open(path) as img:
        img = resize_to_max(img, HERO_MAX_WIDTH)
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        img.save(path, "PNG", optimize=True)
    return path


def main():
    if not os.path.isdir(IMG_DIR):
        print(f"No img/ directory found at {IMG_DIR}")
        return
    print(f"Optimizing images in {IMG_DIR}\n")
    total_before = 0
    total_after = 0
    for name in os.listdir(IMG_DIR):
        path = os.path.join(IMG_DIR, name)
        if not os.path.isfile(path):
            continue
        try:
            size_before = os.path.getsize(path)
            total_before += size_before
            low = name.lower()
            if low == "hero-bread.png" or low == "hero-bread.jpg":
                # Skip hero: often JPEG-in-PNG; optimizing as PNG can increase size
                continue
            elif low.endswith((".jpeg", ".jpg")):
                optimize_jpeg(path)
            else:
                continue
            size_after = os.path.getsize(path)
            total_after += size_after
            pct = (1 - size_after / size_before) * 100 if size_before else 0
            print(f"  {name}: {size_before // 1024} KB -> {size_after // 1024} KB (-{pct:.0f}%)")
        except Exception as e:
            print(f"  {name}: skip ({e})")
    if total_after:
        pct = (1 - total_after / total_before) * 100
        print(f"Total: {total_before // 1024} KB -> {total_after // 1024} KB (-{pct:.0f}%)")


if __name__ == "__main__":
    main()

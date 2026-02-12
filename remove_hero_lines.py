#!/usr/bin/env python3
"""Remove dashed vertical layout lines from hero image."""
from PIL import Image
import os

img_path = os.path.join(os.path.dirname(__file__), "img", "hero-bread.png")
img = Image.open(img_path).convert("RGBA")
pix = img.load()
w, h = img.size

# Line positions: vertical dashed lines at ~20% and ~80% from left
# Use wider bands and sample from farther away for cleaner result
left_center = int(w * 0.20)
right_center = int(w * 0.80)
band_width = max(8, int(w * 0.04))   # wider strip to fully cover dashed lines
source_offset = max(12, int(w * 0.05))  # copy from cleaner area farther from line

def overwrite_vertical_band(x_center, copy_from_offset):
    """Overwrite a vertical band by copying from a column offset to the side."""
    x_start = max(0, x_center - band_width // 2)
    x_end = min(w, x_center + band_width // 2)
    for x in range(x_start, x_end):
        src_x = x + copy_from_offset
        if 0 <= src_x < w:
            for y in range(h):
                pix[x, y] = pix[src_x, y]

# Left line: copy from pixels to the right (positive offset) over the line
overwrite_vertical_band(left_center, source_offset)
# Right line: copy from pixels to the left (negative offset) over the line
overwrite_vertical_band(right_center, -source_offset)

img.save(img_path, "PNG")
print("Saved", img_path)

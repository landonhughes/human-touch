"""Verify delivered GIF timing, loop flags, and exact decoded endpoint equality.
Requires Pillow: python -m pip install Pillow
"""
from pathlib import Path
from PIL import Image, ImageChops
root = Path(__file__).resolve().parents[1]
for variant in ('without-skill', 'with-skill'):
    path = root / variant / 'bunny-loop.gif'
    with Image.open(path) as image:
        assert image.size == (720, 720), image.size
        assert image.n_frames == 200, image.n_frames
        assert image.info.get('loop') == 0, 'GIF must repeat indefinitely'
        first = image.convert('RGB')
        duration = 0
        for frame in range(image.n_frames):
            image.seek(frame)
            duration += image.info.get('duration', 0)
        assert duration == 8000, duration
        assert ImageChops.difference(first, image.convert('RGB')).getbbox() is None, 'Loop seam differs'
    print(f'{variant}: 720 × 720, 200 frames, 8 seconds, infinite loop, exact decoded seam match.')

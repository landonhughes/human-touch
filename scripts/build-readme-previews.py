"""Build small README previews while keeping linked originals untouched."""
from pathlib import Path
import re
import shutil
import subprocess

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
PREVIEWS = ROOT / 'examples' / 'previews'
PNG_STEMS = {'polar-mascot', 'pixel-art-lion', 'oversoul-capsule'}

text = README.read_text()
links = re.findall(r'<a href="(examples/[^"]+\.png)"><img src="([^"]+)"', text)
for relative, current_preview in dict(links).items():
    source = ROOT / relative
    variant = source.parent.name
    stem = source.stem
    width = 700 if stem == 'readfree-app' else 800 if stem in PNG_STEMS else 960
    with Image.open(source) as original:
        original.load()
        width = min(width, original.width)
        height = round(original.height * width / original.width)
        resample = Image.Resampling.NEAREST if stem in {'pixel-art-lion', 'oversoul-capsule'} else Image.Resampling.LANCZOS
        thumbnail = original.resize((width, height), resample)
        if stem in PNG_STEMS:
            destination = PREVIEWS / variant / f'{stem}.png'
            destination.parent.mkdir(parents=True, exist_ok=True)
            thumbnail.save(destination, optimize=True, compress_level=9)
        else:
            destination = PREVIEWS / variant / f'{stem}.jpg'
            destination.parent.mkdir(parents=True, exist_ok=True)
            thumbnail.convert('RGB').save(destination, quality=84, subsampling=0,
                                          progressive=True, optimize=True)
    preview = destination.relative_to(ROOT).as_posix()
    text = text.replace(f'<img src="{current_preview}"', f'<img src="{preview}"')
# The Yolo GIFs stay animated on GitHub. The full-size versions remain in
# examples/{variant}/ and are used by the local gallery.
for variant in ('without-skill', 'with-skill'):
    source = ROOT / 'examples' / variant / 'yolo-ad.gif'
    destination = PREVIEWS / variant / 'yolo-ad.gif'
    if shutil.which('ffmpeg'):
        subprocess.run([
            'ffmpeg', '-loglevel', 'error', '-y', '-i', str(source),
            '-filter_complex',
            '[0:v]fps=10,scale=360:360:flags=lanczos,split[a][b];'
            '[a]palettegen=max_colors=128:stats_mode=diff[p];'
            '[b][p]paletteuse=dither=bayer:bayer_scale=3',
            '-loop', '0', str(destination),
        ], check=True)
    elif not destination.is_file():
        raise RuntimeError('ffmpeg is required to create the animated README previews')
    text = text.replace(f'<img src="examples/{variant}/yolo-ad.gif"',
                        f'<img src="examples/previews/{variant}/yolo-ad.gif"')
README.write_text(text)

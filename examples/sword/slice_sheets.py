"""Slice the existing artwork and build previews. Requires Pillow; run from anywhere."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SIZE = (576, 512)
DURATIONS = [300, 140, 160, 90, 110, 120, 150, 300]

for variant in ('without-skill', 'with-skill'):
    sheet = Image.open(ROOT / variant / 'sword-spritesheet.png').convert('RGBA')
    output = ROOT / variant / 'sword-frames'
    output.mkdir(exist_ok=True)
    frames = []
    # The generated sheet is not an exact grid: the directed slash crosses
    # the nominal first cell boundary. These cuts fall in transparent gutters.
    rows = [(0, 443, [0, 443, 887, 1330, 1774]),
            (443, 887, [0, 465, 935, 1330, 1774])]
    for top, bottom, cuts in rows:
        for left, right in zip(cuts, cuts[1:]):
            sprite = sheet.crop((left, top, right, bottom))
            mask = sprite.getchannel('A').point(lambda a: 255 if a >= 32 else 0)
            bounds = mask.getbbox()
            assert bounds, 'Empty frame'
            sprite = sprite.crop(bounds)
            # Align by the midpoint of the boots, not sword/hair bounds.
            feet = sprite.getchannel('A').crop((0, sprite.height - 18, sprite.width, sprite.height))
            foot_box = feet.point(lambda a: 255 if a >= 128 else 0).getbbox()
            anchor = (foot_box[0] + foot_box[2]) // 2
            x, y = 256 - anchor, 480 - sprite.height
            assert x >= 0 and y >= 0 and x + sprite.width <= SIZE[0]
            frame = Image.new('RGBA', SIZE)
            frame.paste(sprite, (x, y))
            frame.save(output / f'{len(frames) + 1:02}.png')
            frames.append(frame)
    # One palette across all frames prevents palette flicker. Reserve index 255
    # for GIF's binary transparency; PNG frames retain the source alpha.
    atlas = Image.new('RGB', (SIZE[0] * 8, SIZE[1]), (24, 28, 36))
    for i, frame in enumerate(frames):
        atlas.paste(frame, (SIZE[0] * i, 0), frame)
    palette = atlas.quantize(colors=255, method=Image.Quantize.MEDIANCUT)
    indexed = []
    for frame in frames:
        rgb = Image.new('RGB', SIZE, (24, 28, 36))
        rgb.paste(frame, mask=frame.getchannel('A'))
        item = rgb.quantize(palette=palette, dither=Image.Dither.NONE)
        item.paste(255, mask=frame.getchannel('A').point(lambda a: 255 if a < 128 else 0))
        item.info['transparency'] = 255
        indexed.append(item)
    indexed[0].save(ROOT / variant / 'sword-swing.gif', save_all=True,
                    append_images=indexed[1:], duration=DURATIONS,
                    loop=0, transparency=255, disposal=2, optimize=False)
    print(f'{variant}: {len(frames)} frames, {sum(DURATIONS)} ms loop')

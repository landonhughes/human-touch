"""Rebuild the two standalone Hyperframes compositions from shared SVG/motion sources."""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
svg=(root/'scene.svg').read_text()
js=(root/'motion.js').read_text()
for variant in ['without-skill','with-skill']:
    project=root/variant
    (project/'index.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=720,height=720"><title>Carrot intermission — {variant}</title><script src="assets/gsap.min.js"></script><style>*{{box-sizing:border-box;margin:0}}html,body{{width:720px;height:720px;overflow:hidden;background:#f7ece4}}#root{{position:relative;width:100%;height:100%;overflow:hidden}}.clip{{position:absolute;inset:0}}svg{{display:block;width:100%;height:100%}}</style></head><body data-variant="{variant}"><main id="root" data-composition-id="main" data-start="0" data-duration="8" data-width="720" data-height="720"><section class="clip" id="bunny-scene" data-start="0" data-duration="8" data-track-index="0">{svg}</section></main><script>{js}</script></body></html>''')
    (project/'index.motion.json').write_text(json.dumps({'duration':8,'assertions':[{'kind':'staysInFrame','selector':'#art'},{'kind':'keepsMoving','withinSelector':'#bunny-scene','maxStaticSec':1.3}]},indent=2)+'\n')

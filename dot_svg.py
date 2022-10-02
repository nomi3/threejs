try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import svgwrite
import numpy as np

def basic_shapes(name):
    base_width = 680
    draw_width = 480
    pixel_size = draw_width/24
    start_up_left = (base_width-draw_width)/2
    dwg = svgwrite.Drawing(filename=name, debug=True, viewBox=f"0 0 {base_width} {base_width}")
    rng = np.random.default_rng()
    position = rng.integers(0, 24, size=(100, 2)).tolist()

    for y in range(24):
        for x in range(24):
            if [x, y] in position:
                color = rng.integers(0, 256, size=3)
                fill = f'rgb({color[0]},{color[1]},{color[2]})'
                dwg.add(dwg.rect(insert=(x*pixel_size+start_up_left, y*pixel_size+start_up_left), size=(pixel_size, pixel_size), fill=fill))
    dwg.save()


if __name__ == '__main__':
    basic_shapes('random_dot.svg')
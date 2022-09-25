import sys

from vispy import gloo
from vispy import app
import numpy as np

VERT_SHADER = """
attribute vec2 a_position;
attribute vec3 color;
uniform float u_size;
varying vec4 v_color;

void main() {
    gl_Position = vec4(a_position, 0.0, 1.0);
    gl_PointSize = u_size;
    v_color = vec4(color, 1.0);
}
"""

FRAG_SHADER = """
varying vec4 v_color;

void main() {
    gl_FragColor = v_color;
}
"""


class Canvas(app.Canvas):
    def __init__(self):
        app.Canvas.__init__(self, keys='interactive')

        ps = self.pixel_scale

        self.program = gloo.Program(VERT_SHADER, FRAG_SHADER)
        data = np.random.uniform(-0.5, 0.5, size=(400, 2))
        print(data.astype(np.float32))
        self.program['a_position'] = data.astype(np.float32)
        self.program['u_size'] = 20.*ps
        self.program['color'] = (1.0, 1.0, 0)

        self.show()

    def on_resize(self, event):
        width, height = event.size
        gloo.set_viewport(0, 0, width, height)

    def on_draw(self, event):
        gloo.clear('white')
        self.program.draw('points')


if __name__ == '__main__':
    canvas = Canvas()
    if sys.flags.interactive != 1:
        app.run()
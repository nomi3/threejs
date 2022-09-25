from vispy import app, gloo
from vispy.gloo import Program

vertex = """
    attribute vec3 color;
    attribute vec2 position;
    varying vec4 v_color;
    void main()
    {
        gl_Position = vec4(position, 0.0, 1.0);
        v_color = vec4(color, 1.0);
    } """

fragment = """
    varying vec4 v_color;
    void main()
    {
        gl_FragColor = v_color;
    } """


class Canvas(app.Canvas):
    def __init__(self):
        super().__init__(
            size=(512, 512),
            title='Colored quad',
            keys='interactive'
        )

        # Build program
        self.program = Program(vertex, fragment, count=5)

        # Set uniforms and attributes
        self.program['color'] = [
            (1, 0.2, 0), (0, 1, 0),
            (0, 0, 1), (1, 1, 0), (0.2, 0.2, 0)
        ]
        self.program['position'] = [
            (-1, -1), (-1, +1),
            (+1, -1), (+1, +1), (0, 0)
        ]

        gloo.set_viewport(0, 0, *self.physical_size)

        self.show()

    def on_draw(self, event):
        gloo.clear()
        self.program.draw('triangle_strip')

    def on_resize(self, event):
        gloo.set_viewport(0, 0, *event.physical_size)

if __name__ == '__main__':
    c = Canvas()
    app.run()
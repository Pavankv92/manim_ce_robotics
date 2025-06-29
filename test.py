from manim import *


class CreateCircle(Scene):
    def construct(self):
        # show the circle on screen
        mob = Circle(fill_opacity=1, fill_color=BLUE, stroke_color=YELLOW)
        self.play(Create(mob))


class Example(ZoomedScene):
    def construct(self):
        number_plane = NumberPlane(  # HEREFROM
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            stroke_width=100,
            axis_config={
                "stroke_color": YELLOW,
                "stroke_width": 20,
            },
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 15,
                "stroke_opacity": 1,
            },
        )
        self.add(number_plane)  # HERETO
        self.camera.frame.scale(1 / 2)

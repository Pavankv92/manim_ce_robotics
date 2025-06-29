from manim import *


class CreateCircle(Scene):
    def construct(self):
        # show the circle on screen
        circle = Circle(fill_opacity=1, fill_color=BLUE, stroke_color=YELLOW)
        self.play(Create(circle))

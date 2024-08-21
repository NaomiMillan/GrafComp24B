from manim import *

class Figuras(Scene):

    def construct(self):
        sq = Square()
        circ = Circle().set_fill(opacity=1)
        self.play(Transform(sq, circ))
        self.wait()

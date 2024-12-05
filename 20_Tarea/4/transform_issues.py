from manim import *

class VideoCompleto(Scene):
    def construct(self):
        # PORTADA
        self.camera.background_color = " #b5ccf5 "

        titulo = Text(
            "Jessica Naomi Millan Sánchez", 
            font_size=50, 
            gradient=(" #0959e5 ", " #3172e5 ", " #5789e0 ")
        )
        self.play(Write(titulo, run_time=2))
        self.play(titulo.animate.scale(1.2).set_color_by_gradient(" #0959e5 ", " #3172e5 "))
        self.wait(1)
        self.play(FadeOut(titulo, scale=0.8))

        informacion_curso = VGroup(
            Text("Graficación Computacional", font_size=40, gradient=(" #0959e5 ", " #3172e5 ", " #5789e0 ")),
            Text("7mo Semestre 2024B", font_size=35, gradient=(" #0959e5 ", " #3172e5 ", " #5789e0 "))
        ).arrange(DOWN, buff=0.6)
        self.play(FadeIn(informacion_curso[0], shift=UP, run_time=1.5))
        self.play(FadeIn(informacion_curso[1], shift=DOWN, run_time=1.5))
        self.wait(2)
        self.play(FadeOut(informacion_curso, shift=DOWN, scale=1.2))

class TransformationText1V1(Scene):
    def construct(self):
        self.camera.background_color = PURPLE
        texto1 = Text("First text")
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()

class TransformationText1V2(Scene):
    def construct(self):
        self.camera.background_color = BLUE
        texto1 = Text("First text").to_edge(UP)
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()

class TransformationText2(Scene):
    def construct(self):
        self.camera.background_color = GREEN
        text1 = Text("Function")
        text2 = Text("Derivative")
        text3 = Text("Integral")
        text4 = Text("Transformation")

        self.play(Write(text1))
        self.wait()
        self.play(ReplacementTransform(text1, text2))
        self.wait()
        self.play(ReplacementTransform(text2, text3))
        self.wait()
        self.play(ReplacementTransform(text3, text4))
        self.wait()

class CopyTextV1(Scene):
    def construct(self):
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", 
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        ).scale(2)
        self.camera.background_color = BLUE
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9])
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10])
        )
        self.wait()

class CopyTextV2(Scene):
    def construct(self):
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", 
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        ).scale(2)
        self.camera.background_color = BLACK
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()

class CopyTextV3(Scene):
    def construct(self):
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", 
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        ).scale(2)

        formula[8].set_color(RED)
        formula[11].set_color(BLUE)

        self.camera.background_color = GREEN
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()

class ChangeTextColorAnimation(Scene):
    def construct(self):
        self.camera.background_color =RED
        text = Text("Text").scale(3)
        self.play(Write(text))
        self.wait()
        self.play(text.animate.set_color(YELLOW), run_time=2)
        self.wait()

class ChangeSizeAnimation(Scene):
    def construct(self):
        self.camera.background_color = PINK
        text = Text("Text").scale(2)
        self.play(Write(text))
        self.wait()
        self.play(text.animate.scale(1.5), run_time=2)
        self.wait()

class MoveText(Scene):
    def construct(self):
        self.camera.background_color = ORANGE
        text = Text("Text").scale(2).shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        self.play(text.animate.shift(RIGHT * 2), run_time=2, path_arc=0)
        self.wait()

class ChangeColorAndSizeAnimation(Scene):
    def construct(self):
        self.camera.background_color = RED
        text = Text("Text").scale(2).shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.shift(RIGHT * 2).scale(2).set_color(RED),
            run_time=2
        )
        self.wait()

class TextLike1DArrays(Scene):
    def construct(self):
        text1 = Text("Te")
        text2 = Text("xt")
        text2.next_to(text1, RIGHT)
        self.play(FadeIn(text1))
        self.wait(0.5)
        self.play(FadeOut(text1))
        self.play(FadeIn(text2))
        self.wait(0.5)
        self.play(FadeOut(text2))

class TextLike2DArraysV1(Scene):
    def construct(self):
        text = [
            [Text("T"), Text("e")],
            [Text("x"), Text("t")]
        ]
        text[0][0].shift(LEFT + UP)
        text[0][1].next_to(text[0][0], RIGHT)
        text[1][0].next_to(text[0][0], DOWN)
        text[1][1].next_to(text[1][0], RIGHT)
        self.play(FadeIn(text[0][0]))
        self.play(FadeIn(text[0][1]))
        self.play(FadeIn(text[1][0]))
        self.play(FadeIn(text[1][1]))
        self.wait()

class TextLike2DArraysV2(Scene):
    def construct(self):
        text1 = Text("Te")
        text2 = Text("xt")
        text2.next_to(text1, RIGHT, buff=0.2)
        for char in text1:
            self.play(FadeIn(char))
        for char in text2:
            self.play(FadeIn(char))
        self.wait()

class TextLike2DArraysV3(Scene):
    def construct(self):
        text = [Text("Te"), Text("xt")]
        text[1].next_to(text[0], RIGHT, buff=0.2)
        for part in text:
            for char in part:
                self.play(FadeIn(char))
        self.wait()

class TransformIssues(Scene):
    def construct(self):
        text_1 = VGroup(Text("A"), Text("B"), Text("C"))
        text_2 = Text("B")
        text_1.arrange(RIGHT, buff=0.5)
        text_2.next_to(text_1, UP, buff=1)
        self.play(
            *[
                FadeIn(text_1[i])
                for i in [0, 2]
            ],
            FadeIn(text_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(text_2, text_1[1])
        )
        self.wait()

class TransformVGroup(Scene):
    def construct(self):
        text_n = Text("A")
        text_v = VGroup(Text("A")).next_to(text_n, DOWN)
        self.play(Write(text_n))
        self.play(ReplacementTransform(text_n, text_v[0]))
        self.wait()

class TransformIssuesSolution1(Scene):
    def construct(self):
        text_1 = Text("ABC")
        text_2 = Text("B")
        text_2.next_to(text_1, UP, buff=1)
        self.play(
            *[
                FadeIn(text_1[i])
                for i in [0, 2]
            ],
            FadeIn(text_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(text_2, text_1[1])
        )
        self.wait()

class TransformIssuesSolutionInfallible(Scene):
    def construct(self):
        text_1 = Text("ABC")
        text_2 = Text("B")
        text_2.next_to(text_1, UP, buff=1)
        text_1_1_c = Text("B") \
            .match_style(text_1[1]) \
            .match_width(text_1[1]) \
            .move_to(text_1[1])
        self.play(
            *[
                FadeIn(text_1[i])
                for i in [0, 2]
            ],
            FadeIn(text_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(text_2, text_1_1_c)
        )
        self.remove(text_1_1_c)
        self.add(text_1[1])
        self.wait()

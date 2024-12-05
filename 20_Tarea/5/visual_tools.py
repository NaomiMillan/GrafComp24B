from manim import *

class VideoCompleto(Scene):
    def construct(self):
        # PORTADA
        self.camera.background_color = "  #540a3c "

        titulo = Text(
            "Jessica Naomi Millan Sánchez", 
            font_size=50, 
            gradient=("  #cd0e91 ", " #ec48b8 ", "  #ef82cc  ")
        )
        self.play(Write(titulo, run_time=2))
        self.play(titulo.animate.scale(1.2).set_color_by_gradient("  #cd0e91 ", " #ec48b8 ",))
        self.wait(1)
        self.play(FadeOut(titulo, scale=0.8))

        informacion_curso = VGroup(
            Text("Graficación Computacional", font_size=40, gradient=("  #cd0e91 ", " #ec48b8 ", "  #ef82cc  ")),
            Text("7mo Semestre 2024B", font_size=35, gradient=("  #cd0e91 ", " #ec48b8 ", "  #ef82cc  "))
        ).arrange(DOWN, buff=0.6)
        self.play(FadeIn(informacion_curso[0], shift=UP, run_time=1.5))
        self.play(FadeIn(informacion_curso[1], shift=DOWN, run_time=1.5))
        self.wait(2)
        self.play(FadeOut(informacion_curso, shift=DOWN, scale=1.2))
        
 


class MoveBraces(Scene):
    def construct(self):
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=",  # 0
            r"f(x)\frac{d}{dx}g(x)",   # 1
            r"+",                      # 2
            r"g(x)\frac{d}{dx}f(x)"    # 3
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text(r"$g'f$")
        t2 = brace2.get_text(r"$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
        )
        self.wait()
        self.play(
            ReplacementTransform(brace1, brace2),
            ReplacementTransform(t1, t2),
        )
        self.wait()


class MoveBracesCopy(Scene):
    def construct(self):
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", r"+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text(r"$g'f$")
        t2 = brace2.get_text(r"$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
        )
        self.wait()
        self.play(
            ReplacementTransform(brace1.copy(), brace2),
            ReplacementTransform(t1.copy(), t2),
        )
        self.wait()


class MoveFrameBox(Scene):
    def construct(self):
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", r"+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(
            ReplacementTransform(framebox1, framebox2),
        )
        self.wait()


class MoveFrameBoxCopy(Scene):
    def construct(self):
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", r"+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(
            ReplacementTransform(framebox1.copy(), framebox2, path_arc=-PI),
        )
        self.wait()


class MoveFrameBoxCopy2(Scene):
    def construct(self):
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", r"+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        t1 = MathTex(r"g'f")
        t2 = MathTex(r"f'g")
        t1.next_to(framebox1, UP, buff=0.1)
        t2.next_to(framebox2, UP, buff=0.1)
        self.play(
            Create(framebox1),
            FadeIn(t1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1.copy(), framebox2),
            ReplacementTransform(t1.copy(), t2),
        )
        self.wait()


class Arrow1(Scene):
    def construct(self):
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        arrow = Arrow(LEFT, RIGHT)
        step1.move_to(LEFT * 2)
        arrow.next_to(step1, RIGHT, buff=0.1)
        step2.next_to(arrow, RIGHT, buff=0.1)
        self.play(Write(step1))
        self.wait()
        self.play(GrowArrow(arrow))
        self.play(Write(step2))
        self.wait()


class Arrow2(Scene):
    def construct(self):
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = Arrow(step1.get_right(), step2.get_left(), buff=0.1, color=RED)
        arrow2 = Arrow(step1.get_top(), step2.get_bottom(), buff=0.1, color=BLUE)
        self.play(Write(step1), Write(step2))
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.wait()


class LineAnimation(Scene):
    def construct(self):
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = Line(step1.get_right(), step2.get_left(), buff=0.1, color=RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1, color=BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()


class DashedLineAnimation(Scene):
    def construct(self):
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = DashedLine(step1.get_right(), step2.get_left(), buff=0.1, color=RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1, color=BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()

from manim import *

class VideoCompleto(Scene):
    def construct(self):
        # PORTADA
        self.camera.background_color = "#828a89  "

        titulo = Text(
            "Jessica Naomi Millan Sánchez", 
            font_size=50, 
            gradient=("#C70039 ", " #900C3F ", " #581845 ")
        )
        self.play(Write(titulo, run_time=2))
        self.play(titulo.animate.scale(1.2).set_color_by_gradient(" #900C3F ", " #581845 "))
        self.wait(1)
        self.play(FadeOut(titulo, scale=0.8))

        informacion_curso = VGroup(
            Text("Graficación Computacional", font_size=40, gradient=("#FF0000", "#FFA500", "#FFFF00")),
            Text("7mo Semestre 2024B", font_size=35, gradient=("#FF0000", "#FFA500", "#FFFF00"))
        ).arrange(DOWN, buff=0.6)
        self.play(FadeIn(informacion_curso[0], shift=UP, run_time=1.5))
        self.play(FadeIn(informacion_curso[1], shift=DOWN, run_time=1.5))
        self.wait(2)
        self.play(FadeOut(informacion_curso, shift=DOWN, scale=1.2))
        
        escenas = [
            TextColor(), FormulaColor1(), FormulaColor2(), FormulaColor3(), FormulaColor3Fixed(),
            FormulaColor3Fixed2(), FormulaColor4(), FormulaColor5(), ColorByCaracter(), ColorByCaracterFixed(),
            ListFor(), ForRange1(), ForRange2(), ForTwoVariables(), ChangeSize(), AddAndRemoveText(),
            FadeText(), FadeTextFromDirection(), GrowObjectFromCenter(), ShowCreationObject(),
            ColoringText(), CrossText1(), CrossText2(), FrameBox1(), FrameBox2(), BraceText()
        ]

        for escena in escenas:
            # Renderizar cada escena
            escena.construct()
            self.add(*escena.mobjects)  # Agregar objetos de la escena actual
            self.wait(2)
            self.clear()  # Limpiar la escena para evitar superposiciones

COLOR_P="#3EFC24"

class TextColor(Scene):
    def construct(self):
        text = Tex("A","B","C","D","E","F")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")
        text[5].set_color(COLOR_P)
        self.play(Write(text))
        self.wait(2)

class FormulaColor1(Scene): 
    def construct(self):
        text = MathTex("x","=","{a","\\over","b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")
        self.play(Write(text))
        self.wait(2)

class FormulaColor2(Scene): 
    def construct(self): 
        text = MathTex("x","=","\\frac{a}{b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        self.play(Write(text))
        self.wait(2)

class FormulaColor3(Scene): 
    def construct(self):
        text = MathTex("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(2)

class FormulaColor3Fixed(Scene): 
    def construct(self): 
        text = MathTex("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx.}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(3)

class FormulaColor3Fixed2(Scene): 
    def construct(self): 
        text = MathTex("\\sqrt{","\\int_","{a}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        self.play(Write(text))
        self.wait(3)

class FormulaColor4(Scene): 
    def construct(self): 
        text = MathTex("\\sqrt{","\\int_","{a","+","c}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        text[10].set_color(GRAY)
        text[11].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class FormulaColor5(Scene): 
    def construct(self): 
        text = MathTex("\\sqrt{","\\int_","{a","+","c}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        for i,color in zip(text,[PURPLE,BLUE,GREEN,YELLOW,PINK]):
            i.set_color(color)
        self.play(Write(text))
        self.wait(3)


class ColorByCaracter(Scene):
	def construct(self):
		text = MathTex("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		text.set_color_by_tex("x",RED)
		self.play(Write(text))
		self.wait(2)

class ColorByCaracterFixed(Scene): 
	def construct(self):
		text = MathTex("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		text.set_color_by_tex("x",RED)
		text[6].set_color(RED)
		text[8].set_color(WHITE)
		self.play(Write(text))
		self.wait(2)
	
class ListFor(Scene): 
    def construct(self): 
        text = Tex("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in [0,1,3,4]:
        	text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForRange1(Scene): 
    def construct(self): 
        text = Tex("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in range(3):
        	text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForRange2(Scene): 
    def construct(self): 
        text = Tex("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in range(2,6):
        	text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForTwoVariables(Scene): 
    def construct(self): 
        text = Tex("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i,color in [(2,RED),(4,PINK)]:
        	text[i].set_color(color)
        self.play(Write(text))
        self.wait(3)

class ChangeSize(Scene):
    def construct(self):
        text = MathTex("\\sum_{i=0}^n i=\\frac{n(n+1)}{2}")
        self.add(text)
        self.wait()
        text.scale(2) 
        self.wait(2)

class AddAndRemoveText(Scene):
    def construct(self):
        text = Tex("Text or object")
        self.wait()
        self.add(text)
        self.wait()
        self.remove(text)
        self.wait()

class FadeText(Scene):
    def construct(self):
        text = Tex("Text or object")
        self.play(FadeIn(text))
        self.wait()
        self.play(FadeOut(text),run_time=1)
        self.wait()

class FadeTextFromDirection(Scene):
    def construct(self):
        text = Tex("Text or object")
        text.move_to(UP) 
        self.play(FadeIn(text, shift=DOWN), run_time=1) 
        self.wait()

class GrowObjectFromCenter(Scene):
    def construct(self):
        text = Tex("Text or object")
        self.play(GrowFromCenter(text),run_time=1)
        self.wait()

class ShowCreationObject(Scene):
    def construct(self):
        text = Tex("Text or object")
        self.play(Create(text), run_time=1) 
        self.wait()

class ColoringText(Scene):
    def construct(self):
        text = Tex("Text or object")
        self.add(text)
        self.wait(0.5)
        animations = [
            ApplyMethod(letter.set_color, YELLOW)
            for letter in text
        ]

        self.play(LaggedStart(*animations, lag_ratio=0.12))
        self.wait(0.5)

class CrossText1(Scene):
    def construct(self):
        text = Tex(r"$\sum_{i=1}^{\infty}i$", r"$=$", r"$-\frac{1}{2}$")
        cross = Cross(text[2]) 
        cross.set_stroke(RED, 6)
        
        self.play(Write(text)) 
        self.wait(0.5)
        self.play(FadeIn(cross))  
        self.wait(2)

class CrossText2(Scene):
    def construct(self):
        text = Tex(r"$\sum_{i=1}^{\infty}i$", r"$=$", r"$-\frac{1}{2}$")
        
        eq = VGroup(text[1], text[2])
        cross = Cross(eq)
        cross.set_stroke(RED, 6)
        
        self.play(Write(text))
        self.wait(0.5)
        self.play(FadeIn(cross))
        self.wait(2)

class FrameBox1(Scene):
    def construct(self):
        text = MathTex(
            "\\hat{g}(", "f", ")", "=", "\\int", "{t_1}", "^{t{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        frameBox = SurroundingRectangle(text[4], buff=0.5 * SMALL_BUFF)
        self.play(Write(text))
        self.wait(0.5)
        self.play(Create(frameBox)) 
        self.wait(2)

class FrameBox2(Scene):
    def construct(self):
        text = MathTex(
            "\\hat{g}(", "f", ")", "=", "\\int", "{t_1}", "^{t{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        seleccion = VGroup(text[4], text[5], text[6])  
        frameBox = SurroundingRectangle(seleccion, buff=0.5 * SMALL_BUFF)
        frameBox.set_stroke(GREEN, 9) 
        self.play(Write(text))
        self.wait(0.5)
        self.play(Create(frameBox)) 
        self.wait(2)

class BraceText(Scene):
    def construct(self):
        text = Tex(
            r"$\frac{d}{dx}f(x)g(x)=$", r"$f(x)\frac{d}{dx}g(x)$", r"$+$",
            r"$g(x)\frac{d}{dx}f(x)$"
        )
        self.play(Write(text))
        brace_top = Brace(text[1], UP, buff=SMALL_BUFF)
        brace_bottom = Brace(text[3], DOWN, buff=SMALL_BUFF)
        text_top = brace_top.get_text(r"$g'f$")
        text_bottom = brace_bottom.get_text(r"$f'g$")
        self.play(
            GrowFromCenter(brace_top),
            GrowFromCenter(brace_bottom),
            FadeIn(text_top),
            FadeIn(text_bottom)
        )
        self.wait()

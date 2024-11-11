from manim import *

class AllShapes(Scene):
    def construct(self):
        # Nombre
        texto = Text("Jessica Naomi Millan Sánchez", color=WHITE)
        self.play(Create(texto))
        self.wait(1)  # Pausa para que el texto se vea antes de desvanecerse
        self.play(FadeOut(texto))
        
        # Animación de figuras con colores predefinidos de Manim
        self.anim(Arc(radius=0.5, color=BLUE))  # Azul
        self.anim(ArcBetweenPoints([2, 0, 0], [-2, 0, 0], color=GREEN))  # Verde
        self.anim(CurvedArrow([2, 0, 0], [-2, 0, 0], color=RED))  # Rojo
        self.anim(CurvedDoubleArrow([2, 0, 0], [-2, 0, 0], color=ORANGE))  # Naranja
        self.anim(Circle(color=PINK, fill_opacity=1))  # Rosa
        self.anim(Dot(color=YELLOW, fill_opacity=1))  # Amarillo
        self.anim(Dot(radius=0.05, color=PURPLE, fill_opacity=1))  # Púrpura
        self.anim(Ellipse(color=MAROON, fill_opacity=1))  # Granate
        self.anim(AnnularSector(color=GOLD, fill_opacity=1))  # Dorado
        self.anim(Sector(color=TEAL, fill_opacity=1))  # Verde azulado
        self.anim(Annulus(color=ORANGE, fill_opacity=1))  # Naranja
        self.anim(Line([2, 0, 0], [-2, 0, 0], color=WHITE, fill_opacity=1))  # Blanco
        self.anim(DashedLine([2, 0, 0], [-2, 0, 0], color=PURPLE, fill_opacity=1))  # Púrpura

        # Línea tangente que requiere un mobject
        c = Circle(color=BLUE, fill_opacity=1)  # Azul
        self.play(Create(c))  
        self.wait(1)  # Pausa para que el círculo sea visible
        self.anim(TangentLine(c, 0.2))  
        self.play(FadeOut(c))  

        # Otras figuras geométricas con colores predefinidos
        self.anim(Elbow(color=RED))  # Rojo
        self.anim(Arrow([2, 0, 0], [-2, 0, 0], color=GREEN))  # Verde
        self.anim(Vector([1, 0, 0], color=ORANGE, fill_opacity=1))  # Naranja
        self.anim(DoubleArrow([2, 0, 0], [-2, 0, 0], color=PURPLE, fill_opacity=1))  # Púrpura
        self.anim(Polygon([2, 0, 0], [-2, 0, 0], [1, 1, 0], [-2, -3, 0], color=YELLOW, fill_opacity=1))  # Amarillo
        self.anim(RegularPolygon(n=5, color=PINK, fill_opacity=1))  # Rosa
        self.anim(Triangle(color=TEAL, fill_opacity=1))  # Verde azulado
        self.anim(ArrowTriangleTip(color=MAROON, fill_opacity=1))  # Granate
        self.anim(Rectangle(color=GOLD, fill_opacity=1))  # Dorado
        self.anim(Square(color=BLUE, fill_opacity=1))  # Azul
        self.anim(RoundedRectangle(color=WHITE, fill_opacity=1))  # Blanco

    # Método para reproducir la creación y desaparición de los objetos
    def anim(self, mob):
        self.play(Create(mob))  
        self.play(FadeOut(mob))  

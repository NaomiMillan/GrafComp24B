# Alumno: Jessica Naomi Millan Sánchez

# Actividad : Programa que aparece y desaparece un circulo, un rectangulo, y 5 cuadrados de diferentes colores


from manim import *

class cuadrados(Scene):
    def construct(self):
        # Circulo
        square = Circle()
        self.play(FadeIn(square))
        self.wait(1)
        self.play(FadeOut(square))
        self.wait(1)

        # Rectangulo
        square = Rectangle()
        square.set_fill(PINK, opacity=0.5)
        self.play(FadeIn(square))
        self.wait(1)
        self.play(FadeOut(square))
        self.wait(1)

        # Crear y posicionar cuadrados
        square1 = Square().set_fill(RED, opacity=0.8).to_corner(UP + LEFT)   
        square2 = Square().set_fill(GREEN, opacity=0.8).to_corner(DOWN + LEFT)  
        square3 = Square().set_fill(BLUE, opacity=0.8).to_corner(UP + RIGHT) 
        square4 = Square().set_fill(YELLOW, opacity=0.8).to_corner(DOWN + RIGHT)  
        square5 = Square().set_fill(PURPLE, opacity=0.8).move_to(ORIGIN)  

        # Aparecen
        self.play(FadeIn(square1), FadeIn(square2), FadeIn(square3), FadeIn(square4), FadeIn(square5))
        self.wait(1)

        # Cambiar color
        self.play(
            square1.animate.set_fill(ORANGE, opacity=1),
            square2.animate.set_fill(PINK, opacity=1),
            square3.animate.set_fill(TEAL, opacity=1),
            square4.animate.set_fill(WHITE, opacity=1),
            square5.animate.set_fill(GOLD, opacity=1),
            run_time=2
        )
        self.wait(1)

        # Desaparecen
        self.play(FadeOut(square1), FadeOut(square2), FadeOut(square3), FadeOut(square4), FadeOut(square5))
        self.wait(1)

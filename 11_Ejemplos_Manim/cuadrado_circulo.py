# Alumno: Jessica Naomi Millan Sánchez

# Programa : Transforma un cuadrado a un circulo


from manim import *

class SquareToCircle(Scene):
    def construct(self):
        # Crear los objetos
        circle = Circle()
        square = Square()
        
        # Transformaciones del cuadrado
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        
        # Establecer el relleno del círculo
        circle.set_fill(PINK, opacity=0.5)

        # Mostrar el cuadrado y luego transformarlo en círculo
        self.play(Create(square))  # ShowCreation -> Create en Manim Community
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
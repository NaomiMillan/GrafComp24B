from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(YELLOW, opacity=3.0)  # set the color and transparency
        circle.set_stroke(BLUE, width=10)
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 2)  # rotate a certain amount

        self.play(Create(circle))  # animate the creation of the square
        self.play(Transform(circle, square))  # interpolate the square into the circle
        self.play(FadeOut(circle))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(GRAY, opacity=0.5)  # set the color and transparency

        circle2 = Circle()  # create a circle
        circle2.set_fill(YELLOW, opacity=3.0)  # set the color and transparency
        circle2.set_stroke(BLUE, width=10)

        square2 = Square()  # create a square
        square2.set_fill(GREEN, opacity=0.5) 

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        """
        square.next_to(ORIGIN, LEFT, buff=3.0)  # coloca el cuadrado en la esquina superior izquierda
        square2.next_to(ORIGIN, RIGHT)  # coloca el segundo cuadrado en la esquina inferior izquierda
        circle.next_to(ORIGIN, UR)  # coloca el círculo en la esquina superior derecha
        circle2.next_to(ORIGIN, DR) 
        """


        
        square.to_corner(UP + LEFT)   # esquina superior izquierda
        circle2.to_corner(DOWN + LEFT)  # esquina inferior izquierda
        circle.to_corner(UP + RIGHT)  # esquina superior derecha
        square2.to_corner(DOWN + RIGHT)

        #square.next_to(circle, LEFT, buff=0.5) 
        #square2.next_to(circle, DOWN, buff=0.5) 
        #circle2.next_to(square, DOWN, buff=0.5)  # set the position
        #circle.next_to(square, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square), Create(circle2),Create(square2) )  # show the shapes on screen
        #self.play(Create(square))
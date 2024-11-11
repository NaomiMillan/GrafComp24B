from manim import *

class PizzaWithGlasses(Scene):
    def construct(self):
        self.camera.background_color = WHITE  # Establecer el fondo a blanco


        ###################################### TITULO #############################################################################################################
        # Crear el título
        title = Text("Integrantes del Equipo", color=BLACK).scale(1.5)  # Escalar el texto para que sea más grande
        title.to_edge(UP)  # Colocar el título en la parte superior

        # Crear los nombres de los integrantes
        member1 = Text("1. Jessica Naomi Millan Sanchez", color=BLACK)
        member2 = Text("2. Cristhoper Ocativo Cruz", color=BLACK)
        member3 = Text("3. Jesus Enrique Lugo Ramirez", color=BLACK)

        # Agrupar los nombres y alinear
        members = VGroup(member1, member2, member3).arrange(DOWN).next_to(title, DOWN, buff=0.5)

        # Añadir título y miembros a la escena
        self.play(Write(title))  # Escribir el título
        self.wait(0.5)  # Esperar un segundo
        self.play(Write(members))  # Escribir los nombres
        self.wait(0.5)  # Esperar antes de finalizar la escena

        # Desaparecer el título y los miembros
        self.play(FadeOut(title), FadeOut(members))  # Desvanecer el título y los nombres
        self.wait(1)  # Esperar un segundo antes de mostrar el nuevo título

        ###################################### PRESENTACION PIZZACHE #############################################################################################################
        # Crear el nuevo título "PIZZACHE"
        pizzache_title = Text("PIZZACHE", color=BLACK, font_size=72)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior



        # Triángulo (Pizza), más pequeño y centrado en la pantalla
        triangle = Polygon([1, 1, 0], [2.5, 4, 0], [4, 1, 0], color="#FAB81A", fill_opacity=0.7).move_to([0, 0, 0])
        
        # Crear el óvalo (borde de la pizza)
        oval = Ellipse(width=3, height=0.5, color='#DA4C0B').move_to([0, -1.5, 0])
        oval.set_fill(color='#DA4C0B', opacity=20)  # Rellenar el óvalo con el color


        # Lentes (cuadrados) ajustados en tamaño y posición
        lente1 = Square(side_length=0.5, color=BLACK, fill_opacity=1).move_to([-0.5, 0.2, 0])
        lente2 = Square(side_length=0.5, color=BLACK, fill_opacity=1).move_to([0.5, 0.2, 0])

        # Conexión entre lentes
        conexion = Rectangle(width=0.5, height=0.1, color=BLACK, fill_opacity=1).move_to([0, 0.2, 0])

        # Peperonis (Círculos) escalados y posicionados
        peperoni1 = Circle(radius=0.25, color='#D01D13', fill_opacity=1).move_to([0, 0.7, 0])
        peperoni2 = Circle(radius=0.25, color='#D01D13', fill_opacity=1).move_to([-0.6, -1, 0])
        peperoni3 = Circle(radius=0.25, color='#D01D13', fill_opacity=1).move_to([0.5, -0.7, 0])

        # Boca (Semicírculo rotado y ajustado)
        boca = Arc(radius=0.25, start_angle=PI, angle=-PI, color=BLACK).rotate(angle=195 * DEGREES).move_to([0, -0.3, 0])

        # Piernas (Rectángulos) escalados y reubicados
        piernaIzquierda = Rectangle(width=0.2, height=0.65, color=BLACK, fill_opacity=1).move_to([-0.5, -2, 0])
        piernaDerecha = Rectangle(width=0.2, height=0.65, color=BLACK, fill_opacity=1).move_to([0.5, -2, 0])

        # MANOS (Rectángulos) escalados y reubicados
        manoIzquierda = Rectangle(width=1, height=0.1, color=BLACK, fill_opacity=1).move_to([-1.2, -0.5, 0])
        manoDerecha = Rectangle(width=1, height=0.1, color=BLACK, fill_opacity=1).move_to([1.2, -0.5, 0])
        # Rotar los rectángulos
        manoIzquierda.rotate(PI / 6)  # Rotar mano1 30 grados (PI/6 radianes)
        manoDerecha.rotate(-PI / 6)  # Rotar mano2 -30 grados (-PI/6 radianes)

        # Agrupar todos los elementos
        pizza = VGroup(pizzache_title, triangle, oval, lente1, lente2, conexion, peperoni1, peperoni2, peperoni3, boca, piernaIzquierda, piernaDerecha,manoIzquierda, manoDerecha)

        # Escalar todo el grupo de la pizza para que sea más pequeño
        pizza.scale(0.75)

        # Animar la aparición y desaparición de la pizza
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))

















        pizzache_title = Text("Pie Izquierdo", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        pizza = VGroup(pizzache_title,piernaIzquierda)
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))




        pizzache_title = Text("Pie Izquierdo y Derecho", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        pizza = VGroup(pizzache_title,piernaIzquierda, piernaDerecha)
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))


        pizzache_title = Text("Cuerpo", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        pizza = VGroup(pizzache_title,piernaIzquierda, piernaDerecha,triangle,oval,peperoni1, peperoni2, peperoni3)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))

        pizzache_title = Text("Brazo Izquierdo", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        pizza = VGroup(pizzache_title,piernaIzquierda, piernaDerecha,triangle,oval,peperoni1, peperoni2, peperoni3,manoIzquierda)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))




        pizzache_title = Text("Brazo Derecho", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        pizza = VGroup(pizzache_title,piernaIzquierda, piernaDerecha,triangle,oval,peperoni1, peperoni2, peperoni3,manoIzquierda, manoDerecha)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))


        pizzache_title = Text("Boca", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        pizza = VGroup(pizzache_title,piernaIzquierda, piernaDerecha,triangle,oval,peperoni1, peperoni2, peperoni3,manoIzquierda, manoDerecha,boca)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))


        pizzache_title = Text("Ojo Derecho", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        pizza = VGroup(pizzache_title,piernaIzquierda, piernaDerecha,triangle,oval,peperoni1, peperoni2, peperoni3,manoIzquierda, manoDerecha,boca, lente2)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))

        pizzache_title = Text("Ojo Izquierdo y frente de pizzache", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superio
        pizza = VGroup(pizzache_title,piernaIzquierda, piernaDerecha,triangle,oval,peperoni1, peperoni2, peperoni3,manoIzquierda, manoDerecha,boca, lente2, lente1, conexion)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))


        pizzache_title = Text("Parte Trasera de Pizzache", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        pizza = VGroup(pizzache_title,piernaIzquierda, piernaDerecha,triangle,oval,manoIzquierda, manoDerecha)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))



        pizzache_title = Text("Lado Derecho", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior

        # Triángulo (Pizza), más pequeño y centrado en la pantalla
        triangle = Polygon([2, 1, 0], [2.5, 4, 0], [3, 1, 0], color="#FAB81A", fill_opacity=0.7).move_to([0, 0, 0])
        
        # Crear el óvalo (borde de la pizza)
        oval = Ellipse(width=1, height=1, color='#DA4C0B').move_to([0, -1.5, 0])
        oval.set_fill(color='#DA4C0B', opacity=20)  # Rellenar el óvalo con el color
        # Piernas (Rectángulos) escalados y reubicados
        piernaIzquierda = Rectangle(width=0.2, height=0.65, color=BLACK, fill_opacity=1).move_to([0, -2, 0])

        # MANOS (Rectángulos) escalados y reubicados
        manoIzquierda = Rectangle(width=1, height=0.1, color=BLACK, fill_opacity=1).move_to([-0.5, -0.5, 0])
        # Rotar los rectángulos
        manoIzquierda.rotate(PI / 6)  # Rotar mano1 30 grados (PI/6 radianes)

        
        pizza = VGroup(pizzache_title,piernaIzquierda ,triangle,oval,manoIzquierda)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))


        pizzache_title = Text("Lado Izquierdo", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        # Triángulo (Pizza), más pequeño y centrado en la pantalla
        triangle = Polygon([2, 1, 0], [2.5, 4, 0], [3, 1, 0], color="#FAB81A", fill_opacity=0.7).move_to([0, 0, 0])
        
        # Crear el óvalo (borde de la pizza)
        oval = Ellipse(width=1, height=1, color='#DA4C0B').move_to([0, -1.5, 0])
        oval.set_fill(color='#DA4C0B', opacity=20)  # Rellenar el óvalo con el color
        # Piernas (Rectángulos) escalados y reubicados
        piernaIzquierda = Rectangle(width=0.2, height=0.65, color=BLACK, fill_opacity=1).move_to([0, -2, 0])

        # MANOS (Rectángulos) escalados y reubicados
        manoIzquierda = Rectangle(width=1, height=0.1, color=BLACK, fill_opacity=1).move_to([0.5, -0.5, 0])
        # Rotar los rectángulos
        manoIzquierda.rotate(-PI / 6)  # Rotar mano1 30 grados (PI/6 radianes)

        
        pizza = VGroup(pizzache_title,piernaIzquierda ,triangle,oval,manoIzquierda)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))


        pizzache_title = Text("Saludo", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superio

        # Triángulo (Pizza), más pequeño y centrado en la pantalla
        triangle = Polygon([1, 1, 0], [2.5, 4, 0], [4, 1, 0], color="#FAB81A", fill_opacity=0.7).move_to([0, 0, 0])
        
        # Crear el óvalo (borde de la pizza)
        oval = Ellipse(width=3, height=0.5, color='#DA4C0B').move_to([0, -1.5, 0])
        oval.set_fill(color='#DA4C0B', opacity=20)  # Rellenar el óvalo con el color


        # Lentes (cuadrados) ajustados en tamaño y posición
        lente1 = Square(side_length=0.5, color=BLACK, fill_opacity=1).move_to([-0.5, 0.2, 0])
        lente2 = Square(side_length=0.5, color=BLACK, fill_opacity=1).move_to([0.5, 0.2, 0])

        # Conexión entre lentes
        conexion = Rectangle(width=0.5, height=0.1, color=BLACK, fill_opacity=1).move_to([0, 0.2, 0])

        # Peperonis (Círculos) escalados y posicionados
        peperoni1 = Circle(radius=0.25, color='#D01D13', fill_opacity=1).move_to([0, 0.7, 0])
        peperoni2 = Circle(radius=0.25, color='#D01D13', fill_opacity=1).move_to([-0.6, -1, 0])
        peperoni3 = Circle(radius=0.25, color='#D01D13', fill_opacity=1).move_to([0.5, -0.7, 0])

        # Boca (Semicírculo rotado y ajustado)
        boca = Arc(radius=0.25, start_angle=PI, angle=-PI, color=BLACK).rotate(angle=195 * DEGREES).move_to([0, -0.3, 0])

        # Piernas (Rectángulos) escalados y reubicados
        piernaIzquierda = Rectangle(width=0.2, height=0.65, color=BLACK, fill_opacity=1).move_to([-0.5, -2, 0])
        piernaDerecha = Rectangle(width=0.2, height=0.65, color=BLACK, fill_opacity=1).move_to([0.5, -2, 0])

        # MANOS (Rectángulos) escalados y reubicados
        manoIzquierda = Rectangle(width=1, height=0.1, color=BLACK, fill_opacity=1).move_to([-1.1, 0, 0])
        manoDerecha = Rectangle(width=1, height=0.1, color=BLACK, fill_opacity=1).move_to([1.2, -0.5, 0])

        manoIzquierda.rotate(-PI /6)  # Rotar mano1 30 grados (PI/6 radianes)        manoDerecha = Rectangle(width=1, height=0.1, color=BLACK, fill_opacity=1).move_to([1.2, -0.5, 0])
        # Rotar los rectángulos
        manoDerecha.rotate(-PI / 6)  # Rotar mano2 -30 grados (-PI/6 radianes)

        pizza = VGroup(pizzache_title,piernaIzquierda, piernaDerecha,triangle,oval,peperoni1, peperoni2, peperoni3,manoIzquierda, manoDerecha,boca, lente2, lente1, conexion)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))






#manim -pql PizzaAnimada.py PizzaWithGlasses
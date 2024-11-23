# Escenarios de la historia de Pizzache

### Trabajo realizado por: Jessica Naomi Millan Sánchez
### Graficación Computacional
### Profesora: Hazem Álvarez Rodríguez
### Clase del 06 de noviembre de 2024

from manim import *

class PizzaWithGlasses(Scene):
    def construct(self):
        self.portada()
        

        self.presentacion()

        title = Text("Parte frontal de Pizzache", color=BLACK).scale(1.5).to_edge(UP)
        enfrente = self.enfrentePizzache()
        g1 = VGroup(title, enfrente)
        self.aparecerDesaparecer(g1)

        title = Text("Parte trasera de Pizzache", color=BLACK).scale(1.5).to_edge(UP)
        atras = self.atrasPizzache()
        g2 = VGroup(title, atras)
        self.aparecerDesaparecer(g2)

        title = Text("lado derecho de Pizzache", color=BLACK).scale(1.5).to_edge(UP)
        derecho = self.ladoDerechoPizzache()
        g3 = VGroup(title, derecho)
        self.aparecerDesaparecer(g3)

        title = Text("lado izquierdo de Pizzache", color=BLACK).scale(1.5).to_edge(UP)
        izquierdo = self.ladoIzquierdoPizzache()
        g4 = VGroup(title, izquierdo)
        self.aparecerDesaparecer(g4)

        titulo = self.introduccionHistoria()
        titulo1 = VGroup(titulo)
        self.aparecerDesaparecer(titulo1)

        title = Text("Presenciamos el nacimiento de una pizza, llamada >pizzache<", color=BLACK).scale(0.5).to_edge(UP)
        caja = self.cajaPizza()
        enfrente = self.enfrentePizzache()
        g5 = VGroup( caja,enfrente, title)
        self.aparecerDesaparecer(g5)

        title = Text("Pero pizzache quería salir y conocer el mundo, así que se fue", color=BLACK).scale(0.5).to_edge(UP)
        puerta = self.puerta()
        atras = self.atrasPizzache()
        g6 = VGroup(puerta, atras, title)
        self.aparecerDesaparecer(g6)

        title = Text("Camino mucho tiempo conociendo diferentes lugares", color=BLACK).scale(0.5).to_edge(UP)
        parque = self.parque()
        derecho = self.ladoDerechoPizzache()
        g7 = VGroup( parque, derecho, title)
        self.aparecerDesaparecer(g7)

        title = Text("hasta que encontró un lugar donde finalmente se sentía cómodo..", color=BLACK).scale(0.5).to_edge(UP)
        pizzeria = self.pizzeria()
        frente = self.enfrentePizzache().scale(0.5).move_to([-1,-3,0])
        g8 = VGroup(pizzeria, frente, title)
        self.aparecerDesaparecer(g8)
        self.despedida()

        
    
    def aparecerDesaparecer(self, objeto):
        self.play(FadeIn(objeto))
        self.wait(3)
        self.play(FadeOut(objeto))

    def introduccionHistoria(self):
        title = Text("Historia de Pizache", color=BLACK).scale(1.5)  # Escalar el texto para que sea más grande
        return title



    def portada(self):
        self.camera.background_color = WHITE  # Establecer el fondo a blanco
        ###################################### TITULO #############################################################################################################
        # Crear el título
        title = Text("Integrantes del Equipo", color=BLACK).scale(1.5)  # Escalar el texto para que sea más grande
        title.to_edge(UP)  # Colocar el título en la parte superior

        # Crear los nombres de los integrantes
        member1 = Text("1. Jessica Naomi Millan Sanchez", color=BLACK)
        member2 = Text("2. Christopher Octavio Tellez Dominguez", color=BLACK)
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


    def presentacion(self):
        self.camera.background_color = WHITE  # Establecer el fondo a blanco


        ###################################### PRESENTACION PIZZACHE #############################################################################################################
        # Crear el nuevo título "PIZZACHE"
        self.pizzache_title = Text("PIZZACHE", color=BLACK, font_size=72)  # Título más grande
        self.pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior



        # Triángulo (Pizza), más pequeño y centrado en la pantalla
        self.triangle = Polygon([1, 1, 0], [2.5, 4, 0], [4, 1, 0], color="#FAB81A", fill_opacity=1).move_to([0, 0, 0])
        
        # Crear el óvalo (borde de la pizza)
        self.oval = Ellipse(width=3, height=0.5, color='#DA4C0B').move_to([0, -1.5, 0])
        self.oval.set_fill(color='#DA4C0B', opacity=20)  # Rellenar el óvalo con el color


        # Lentes (cuadrados) ajustados en tamaño y posición
        self.lente1 = Square(side_length=0.5, color=BLACK, fill_opacity=1).move_to([-0.5, 0.2, 0])
        self.lente2 = Square(side_length=0.5, color=BLACK, fill_opacity=1).move_to([0.5, 0.2, 0])

        # Conexión entre lentes
        self.conexion = Rectangle(width=0.5, height=0.1, color=BLACK, fill_opacity=1).move_to([0, 0.2, 0])

        # Peperonis (Círculos) escalados y posicionados
        self.peperoni1 = Circle(radius=0.25, color='#D01D13', fill_opacity=1).move_to([0, 0.7, 0])
        self.peperoni2 = Circle(radius=0.25, color='#D01D13', fill_opacity=1).move_to([-0.6, -1, 0])
        self.peperoni3 = Circle(radius=0.25, color='#D01D13', fill_opacity=1).move_to([0.5, -0.7, 0])

        # Boca (Semicírculo rotado y ajustado)
        self.boca = Arc(radius=0.25, start_angle=PI, angle=-PI, color=BLACK).rotate(angle=195 * DEGREES).move_to([0, -0.3, 0])

        # Piernas (Rectángulos) escalados y reubicados
        self.piernaIzquierda = Rectangle(width=0.2, height=0.65, color=BLACK, fill_opacity=1).move_to([-0.5, -2, 0])
        self.piernaDerecha = Rectangle(width=0.2, height=0.65, color=BLACK, fill_opacity=1).move_to([0.5, -2, 0])



        # Agrupar todos los elementos
        self.pizza = VGroup(self.pizzache_title, self.triangle, self.oval, self.lente1, self.lente2, self.conexion, self.peperoni1, self.peperoni2, self.peperoni3, self.boca, self.piernaIzquierda, self.piernaDerecha)

        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.pizza.scale(0.75)

        # Animar la aparición y desaparición de la pizza
        self.play(FadeIn(self.pizza))
        self.wait(1)
        self.play(FadeOut(self.pizza))

        self.pizzache_title = Text("Pie Izquierdo", color=BLACK, font_size=50)  # Título más grande
        self.pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        self.pizza = VGroup(self.pizzache_title,self.piernaIzquierda)
        self.play(FadeIn(self.pizza))
        self.wait(1)
        self.play(FadeOut(self.pizza))

        self.pizzache_title = Text("Pie Izquierdo y Derecho", color=BLACK, font_size=50)  # Título más grande
        self.pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        self.pizza = VGroup(self.pizzache_title,self.piernaIzquierda, self.piernaDerecha)
        self.play(FadeIn(self.pizza))
        self.wait(1)
        self.play(FadeOut(self.pizza))


        self.pizzache_title = Text("Cuerpo", color=BLACK, font_size=50)  # Título más grande
        self.pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        self.pizza = VGroup(self.pizzache_title,self.piernaIzquierda, self.piernaDerecha,self.triangle,self.oval,self.peperoni1, self.peperoni2, self.peperoni3)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(self.pizza))
        self.wait(1)
        self.play(FadeOut(self.pizza))

        self.pizzache_title = Text("Boca", color=BLACK, font_size=50)  # Título más grande
        self.pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        self.pizza = VGroup(self.pizzache_title,self.piernaIzquierda, self.piernaDerecha,self.triangle,self.oval,self.peperoni1, self.peperoni2, self.peperoni3,self.boca)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(self.pizza))
        self.wait(1)
        self.play(FadeOut(self.pizza))

        self.pizzache_title = Text("Ojo Derecho", color=BLACK, font_size=50)  # Título más grande
        self.pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superior
        self.pizza = VGroup(self.pizzache_title,self.piernaIzquierda, self.piernaDerecha,self.triangle,self.oval,self.peperoni1, self.peperoni2, self.peperoni3,self.boca, self.lente2)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(self.pizza))
        self.wait(1)
        self.play(FadeOut(self.pizza))

        self.camera.background_color = WHITE  # Establecer el fondo a blanco
        pizzache_title = Text("Ojo Izquierdo y frente de pizzache", color=BLACK, font_size=50)  # Título más grande
        pizzache_title.to_edge(UP)  # Colocar el nuevo título en la parte superio
        pizza = VGroup(pizzache_title,self.piernaIzquierda, self.piernaDerecha,self.triangle,self.oval,self.peperoni1, self.peperoni2, self.peperoni3,self.boca, self.lente2, self.lente1, self.conexion)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        self.play(FadeIn(pizza))
        self.wait(1)
        self.play(FadeOut(pizza))

    
        

    


    def enfrentePizzache(self):
        self.camera.background_color = WHITE  # Establecer el fondo a blanco
        pizza = VGroup(self.piernaIzquierda, self.piernaDerecha,self.triangle,self.oval,self.peperoni1, self.peperoni2, self.peperoni3,self.boca, self.lente2, self.lente1, self.conexion).move_to([0,-2,0])
        # Escalar todo el grupo de la pizza para que sea más pequeño
        return pizza



    def atrasPizzache(self):
        self.camera.background_color = WHITE  # Establecer el fondo a blanco
        
        pizza = VGroup(self.piernaIzquierda, self.piernaDerecha,self.triangle,self.oval).move_to([0,-2,0])
        # Escalar todo el grupo de la pizza para que sea más pequeño
        return pizza



    def ladoDerechoPizzache(self):
        self.camera.background_color = WHITE  # Establecer el fondo a blanco

        # Triángulo (Pizza), más pequeño y centrado en la pantalla
        triangle = Polygon([2, 1, 0], [2.5, 4, 0], [3, 1, 0], color="#FAB81A", fill_opacity=1).move_to([0, 0, 0])
        # Crear el óvalo (borde de la pizza)
        oval = Ellipse(width=1, height=1, color='#DA4C0B').move_to([0, -1.5, 0])
        oval.set_fill(color='#DA4C0B', opacity=20)  # Rellenar el óvalo con el color
        # Piernas (Rectángulos) escalados y reubicados
        piernaIzquierda = Rectangle(width=0.2, height=0.65, color=BLACK, fill_opacity=1).move_to([0, -2, 0])

        pizza = VGroup(piernaIzquierda ,triangle,oval)
        # Escalar todo el grupo de la pizza para que sea más pequeño
        return pizza



    def ladoIzquierdoPizzache(self):
        self.camera.background_color = WHITE  # Establecer el fondo a blanco

        # Triángulo (Pizza), más pequeño y centrado en la pantalla
        triangle = Polygon([2, 1, 0], [2.5, 4, 0], [3, 1, 0], color="#FAB81A", fill_opacity=1).move_to([0, 0, 0])
        
        # Crear el óvalo (borde de la pizza)
        oval = Ellipse(width=1, height=1, color='#DA4C0B').move_to([0, -1.5, 0])
        oval.set_fill(color='#DA4C0B', opacity=20)  # Rellenar el óvalo con el color
        # Piernas (Rectángulos) escalados y reubicados
        piernaIzquierda = Rectangle(width=0.2   , height=0.65, color=BLACK, fill_opacity=1).move_to([0, -2, 0])

        pizza = VGroup(piernaIzquierda ,triangle,oval)
        
        return pizza


    def cajaPizza(self):
        self.camera.background_color = WHITE  # Establecer el fondo a blanco
        tapa1 = Rectangle(width=4, height=4, color="#5e3016", fill_opacity=1).move_to([0, 1, 0])
        tapa2 = Polygon([-2, 0, 0], [2, 0, 0], [1, -3, 0], [-3, -3, 0], color="#5e3016", fill_opacity=1).move_to([-0.5, -2.5, 0])
        tapa3 = Rectangle(width=3.25, height=3.25, color="#755433", fill_opacity=1).move_to([0, 1, 0])
        tapa4 = Polygon([-1.5, 0, 0], [1.5, 0, 0], [0.75, -2.25, 0], [-2.25, -2.25, 0], color="#755433", fill_opacity=1).move_to([-0.5, -2.5, 0])

        grupo1 = VGroup(tapa1,tapa2,tapa3, tapa4)
        #

        return grupo1


    def puerta(self):
        self.camera.background_color = WHITE  # Establecer el fondo a blanco

        puerta = Rectangle(width=4, height=8, color="#5e3016", fill_opacity=1).move_to([0, 0, 0])
        perilla = Circle(radius=0.25, color='#dfe220', fill_opacity=1).move_to([-1.5, 0, 0])

        grupo2 = VGroup(puerta,perilla)

        return grupo2


    def parque(self):

        self.camera.background_color = WHITE  # Establecer el fondo a blanco

        cielo = Rectangle(width=15, height=5, color="#20d5e2", fill_opacity=1).move_to([0, 1.5, 0])
        pasto = Rectangle(width=15, height=3, color="#63e220", fill_opacity=1).move_to([0, -2.5, 0])
        sol = Circle(radius=1, color='#dfe220', fill_opacity=1).move_to([-5.7, 2.75, 0])
        nube1 = Circle(radius=0.75, color='#ffffff', fill_opacity=1).move_to([4.25, 2.75, 0])
        nube2 = Circle(radius=0.75, color='#ffffff', fill_opacity=1).move_to([6, 2.75, 0])
        nube3 = Circle(radius=0.75, color='#ffffff', fill_opacity=1).move_to([5.25, 3, 0])
        nube4 = Circle(radius=0.75, color='#ffffff', fill_opacity=1).move_to([5.25, 2.25, 0])

        

        grupo3 = VGroup(cielo,pasto,sol, nube1, nube2, nube3, nube4)

        return grupo3

    def pizzeria(self):

        self.camera.background_color = WHITE  # Establecer el fondo a blanco

        cuarto = Rectangle(width=4.5, height=4.5, color="#666a6a", fill_opacity=1).move_to([0, -1, 0])
        v1 = Rectangle(width=1, height=1, color="#7ff1f5", fill_opacity=1).move_to([-1, -0.25, 0])
        v2 = Rectangle(width=1, height=1, color="#7ff1f5", fill_opacity=1).move_to([1, -0.25, 0])
        p = Rectangle(width=3, height=1.5, color="#b29364", fill_opacity=1).move_to([0, -2.25, 0])
        perilla1= Circle(radius=0.1, color='#bfae00', fill_opacity=1).move_to([-0.2, -2.25, 0])
        perilla2 = Circle(radius=0.1, color='#bfae00', fill_opacity=1).move_to([0.2, -2.25, 0])
        linea = Line(start=[0, -1.5, 0], end=[0, -3, 0], color=BLACK)

        techo = Polygon([-3, 5, 0],[3, 5, 0], [0,7 , 0], color="#d16f1e", fill_opacity=1).move_to([0, 2, 0])

        letrero = Text("PIZZERIA CHE", color=BLACK).scale(0.5).move_to([0,1.25,0])

        grupo4 = VGroup(cuarto,techo,v1,v2,p,perilla1, perilla2,linea, letrero)

        return grupo4

    def despedida(self):

        self.despedida = Text("FIN", color=BLACK, font_size=72)  # Título más grande

        self.play(Write(self.despedida))  # Escribir los nombres
        self.wait(0.5)  # Esperar antes de finalizar la escena

        # Desaparecer el título y los miembros
        self.play(FadeOut(self.despedida))  # Desvanecer el título y los nombres
        self.wait(0.5)  # Esperar un segundo antes de mostrar el nuevo título


        self.despedida = Text("Gracias por su Atencion", color=BLACK, font_size=72)  # Título más grande
        self.despedida.to_edge(UP)  # Colocar el nuevo título en la parte superior

        self.play(Write(self.despedida))  # Escribir los nombres
        self.wait(1)  # Esperar antes de finalizar la escena

        # Desaparecer el título y los miembros
        self.play(FadeOut(self.despedida))  # Desvanecer el título y los nombres
        self.wait(1)  # Esperar un segundo antes de mostrar el nuevo título










#manim -pql PizzaAnimada.py PizzaWithGlasses


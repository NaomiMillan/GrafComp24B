from manim import *
import numpy as np

class VideoCompleto(Scene):
    def construct(self):
        # PORTADA
        self.camera.background_color = " #d6cef0 "

        titulo = Text(
            "Jessica Naomi Millan Sánchez", 
            font_size=50, 
            gradient=(" #3308ba ", " #6946d6 ", " #9078da ")
        )
        self.play(Write(titulo, run_time=2))
        self.play(titulo.animate.scale(1.2).set_color_by_gradient(" #6946d6 ", " #9078da "))
        self.wait(1)
        self.play(FadeOut(titulo, scale=0.8))

        informacion_curso = VGroup(
            Text("Graficación Computacional", font_size=40, gradient=(" #3308ba ", " #6946d6 ", " #9078da ")),
            Text("7mo Semestre 2024B", font_size=35, gradient=(" #3308ba ", " #6946d6 ", " #9078da "))
        ).arrange(DOWN, buff=0.6)
        self.play(FadeIn(informacion_curso[0], shift=UP, run_time=1.5))
        self.play(FadeIn(informacion_curso[1], shift=DOWN, run_time=1.5))
        self.wait(2)
        self.play(FadeOut(informacion_curso, shift=DOWN, scale=1.2))
        
 

class PlotGraph(Scene):
    def construct(self):
        y_max = 50
        y_min = 20
        x_max = 7
        x_min = 4
        y_tick_frequency = 5
        x_tick_frequency = 0.5
        axes_color = BLUE
        """3 * DOWN + 6 * LEFT"""
    
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
        )
        
        
        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )
        
        axes.x_axis.add_numbers([4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
        axes.y_axis.add_numbers([30, 40, 50])

        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[5, 7]) 

        p = Dot().move_to(axes.c2p(x_min, y_min))
        
        self.add(axes,axes_labels,p)
               
        self.play(Create(graph),
                  run_time=2)
        self.wait() 


class Plot1(Scene):
    def construct(self):
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 5
        x_tick_frequency = 0.5
        axes_color = BLUE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips = False
        )
        
        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )

        axes.x_axis.add_numbers([2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
        axes.y_axis.add_numbers([20, 30, 40, 50])

        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[2, 4])

        self.wait()
        self.play(Write(axes),
                  Write(axes_labels), 
                  run_time=4)
        self.play(Create(graph),
                  run_time=2)
        self.wait()

class Plot1v2(Scene):
    def construct(self):
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 5
        x_tick_frequency = 1
        axes_color = BLUE
        #graph_origin = np.array((0, 0, 0))

        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips = False
        ).scale(0.5) 
        
        axes.to_corner(UR)
        
        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[2, 4])

        self.play(Write(axes),Write(axes_labels), Create(graph), run_time=2)
        self.wait()

class Plot2(Scene):
    def construct(self):
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 5
        x_tick_frequency = 1
        axes_color = BLUE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips = False
        )

        axes.x_axis.add_numbers([2, 3, 4, 5 ,6 ,7])
        axes.y_axis.add_numbers([20, 30, 40, 50])
        
        
        graph = axes.plot(lambda x: x**2, color=GREEN)

        axes_labels = axes.get_axis_labels(
            x_label=Tex("t"),
            y_label=Tex("f(t)")
        )
        
        self.add(axes, axes_labels)

        
        self.play(Write(axes),Write(axes_labels),run_time=2)
        self.play(Create(graph), run_time=2)

        self.wait()

class Plot3(Scene):
    def construct(self):
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 5
        x_tick_frequency = 1
        axes_color = BLUE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips = False
        )

        axes.x_axis.add_numbers([0,2, 4, 5])
        axes.y_axis.add_numbers([0,5,10,15,20,25, 30,35, 40,45, 50])
        
        
        graph = axes.plot(lambda x: x**2, color=GREEN)

        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )
        
        self.add(axes, axes_labels)

        
        self.play(Write(axes),Write(axes_labels),run_time=2)
        self.play(Create(graph), run_time=2)

        self.wait()


class Plot4(Scene):
    def construct(self):
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 10
        x_tick_frequency = 1
        axes_color = BLUE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips = False
        )

        axes.x_axis.add_numbers([3.5,4,5])
        axes.y_axis.add_numbers([0,5,10,15,20,25, 30,35, 40,45, 50])
        
        
        graph = axes.plot(lambda x: x**2, color=GREEN)

        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )
        
        self.add(axes, axes_labels)

        
        self.play(Write(axes),Write(axes_labels),run_time=2)
        self.play(Create(graph), run_time=2)

        self.wait()


class Plot5(Scene):
    def construct(self):
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 10
        x_tick_frequency = 0.5
        axes_color = BLUE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips = False
        )

        x_labels = VGroup()  
        
        label_3_5 = Tex("3.5")
        label_3_5.scale(0.7)
        label_3_5.next_to(axes.coords_to_point(3.5, 0), DOWN)
        x_labels.add(label_3_5)

        
        label_4_5 = MathTex("\\frac{9}{2}")
        label_4_5.scale(0.7)
        label_4_5.next_to(axes.coords_to_point(4.5, 0), DOWN)
        x_labels.add(label_4_5)
        
        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )

        graph = axes.plot(lambda x: x**2, color=GREEN)
        self.play(Write(axes), Write(x_labels),Write(axes_labels))
        self.play(Create(graph))
        
        self.wait()
        
class Plot6(Scene):
    def construct(self):
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 10
        x_tick_frequency = 0.5
        axes_color = BLUE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips = False
        )

        values_x = [
            (0, "0"),
            (0.5, "0.5"),
            (1, "1"),
            (1.5, "1.5"),
            (3.35, "3.35")  ]
        
        for x_val, x_tex in values_x:
            
            tex = MathTex(x_tex) 
            tex.scale(0.7)
            tex.next_to(axes.c2p(x_val, 0), DOWN)  
            self.add(tex)

        graph = axes.plot(lambda x: x**2, color=GREEN)

        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )

        self.add(axes, axes_labels)

        self.play(Write(axes), Write(axes_labels), run_time=2)
        self.play(Create(graph), run_time=2)

        self.wait()

class Plot7(Scene):
    def construct(self):
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 10
        x_tick_frequency = 0.5
        axes_color = BLUE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips = False
        )

        axes.x_axis.add_numbers([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7])
        
        
        graph = axes.plot(lambda x: x**2, color=GREEN)

        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )
        
        self.add(axes, axes_labels)

        
        self.play(Write(axes),Write(axes_labels),run_time=2)
        self.play(Create(graph), run_time=2)

        self.wait()


class PlotSinCos(Scene):
    def construct(self):
        y_max = 1.5
        y_min = -1.5        
        x_max = 3 * np.pi/2
        x_min = -3 * np.pi/2
        y_tick_frequency = 0.5
        x_tick_frequency = np.pi/2
        axes_color = YELLOW
        axes_color_2= RED
        

        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            y_axis_config={"color": axes_color},
            x_axis_config={"color": axes_color_2},
            tips=False
        )

        values_y = [
            (1, "1"),
            (-1, "-1")
        ]
        
        y_labels = VGroup()
        for y_val, y_tex in values_y:
            tex = MathTex(y_tex)
            tex.scale(0.7)
            tex.next_to(axes.c2p(0, y_val), LEFT)
            y_labels.add(tex)

        values_x = [
            ("-\\frac{3\\pi}{2}", -3*np.pi/2),
            ("-\\pi", -np.pi),
            ("-\\frac{\\pi}{2}", -np.pi/2),
            ("0", 0),
            ("\\frac{\\pi}{2}", np.pi/2),
            ("\\pi", np.pi),
            ("\\frac{3\\pi}{2}", 3*np.pi/2),
        ]  

        x_labels = VGroup()
        for label, value in values_x:
            tex = MathTex(label)
            tex.scale(0.7)
            tex.next_to(axes.c2p(value, 0), DOWN)
            x_labels.add(tex)

        plotSin = axes.plot(lambda x: np.sin(x), color=GREEN)
        plotCos = axes.plot(lambda x: np.cos(x), color=GRAY)
        
        axes_labels = axes.get_axis_labels(
            x_label=MathTex("\\theta"),
            y_label=MathTex("\\sin(\\theta)")
        )

        self.add(axes, x_labels, y_labels,axes_labels)
        self.play(Create(plotSin), run_time=2)
        self.play(Create(plotCos), run_time=2)
        self.wait()

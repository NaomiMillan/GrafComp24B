from manim import *

class VideoCompleto(Scene):
    def construct(self):
        # PORTADA
        self.camera.background_color = " #000000"

        titulo = Text(
            "Jessica Naomi Millan Sánchez", 
            font_size=50, 
            gradient=(" #4c7adb", "#4ca7db", " #39afb9 ")
        )
        self.play(Write(titulo, run_time=2))
        self.play(titulo.animate.scale(1.2).set_color_by_gradient(" #4c7adb", "#4ca7db"))
        self.wait(1)
        self.play(FadeOut(titulo, scale=0.8))

        informacion_curso = VGroup(
            Text("Graficación Computacional", font_size=40, gradient=(" #4c7adb", "#4ca7db", " #39afb9 ")),
            Text("7mo Semestre 2024B", font_size=35, gradient=(" #2898d4 ", " #28d4b2 ", " #28d479 "))
        ).arrange(DOWN, buff=0.6)
        self.play(FadeIn(informacion_curso[0], shift=UP, run_time=1.5))
        self.play(FadeIn(informacion_curso[1], shift=DOWN, run_time=1.5))
        self.wait(2)
        self.play(FadeOut(informacion_curso, shift=DOWN, scale=1.2))
        
 


class CameraPosition1(ThreeDScene):
    def construct(self):
        # Añadimos ejes 3D para darle contexto
        axes = ThreeDAxes()
        circulo = Circle()
        self.add(axes)  # Agregamos los ejes
        self.play(Create(circulo))
        self.wait()


class CameraPosition2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=30 * DEGREES, theta=45 * DEGREES)  # Orientación 3D
        self.play(Create(circle), Create(axes))
        self.wait()


class CameraPosition3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()


class CameraPosition4(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-5, 5], y_range=[-5, 5], z_range=[-2, 2])
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6)
        self.play(Create(circle), Create(axes))
        self.wait()


class CameraPosition5(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6, gamma=30 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()


class MoveCamera1(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.add(axes)
        self.play(Create(circle))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait()


class MoveCamera2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES)
        self.add(axes)
        self.play(Create(circle))
        self.begin_ambient_camera_rotation(rate=0.1)  # Rotación continua
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=80 * DEGREES, theta=-PI / 2)  # Volver a posición inicial
        self.wait()

class ParametricCurve1(ThreeDScene):
    def construct(self):
        # Curva paramétrica 1
        curve1_points = np.array([
            [1.2 * np.cos(u), 1.2 * np.sin(u), u / 2]
            for u in np.linspace(-TAU, TAU, 100)  # 100 puntos en el rango [-TAU, TAU]
        ])
        curve1 = VMobject().set_points_as_corners(curve1_points)

        # Curva paramétrica 2
        curve2_points = np.array([
            [1.2 * np.cos(u), 1.2 * np.sin(u), u]
            for u in np.linspace(-TAU, TAU, 100)  # 100 puntos en el rango [-TAU, TAU]
        ])
        curve2 = VMobject().set_points_as_corners(curve2_points)

        # Ejes
        axes = ThreeDAxes()

        # Configuración de cámara
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Animaciones
        self.play(Create(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()

class ParametricCurve2(ThreeDScene):
    def construct(self):
        # Curva paramétrica 1
        curve1_points = np.array([
            [1.2 * np.cos(u), 1.2 * np.sin(u), u / 2]
            for u in np.linspace(-TAU, TAU, 100)  # 100 puntos en el rango [-TAU, TAU]
        ])
        curve1 = VMobject().set_points_as_corners(curve1_points).set_shade_in_3d(True)

        # Curva paramétrica 2
        curve2_points = np.array([
            [1.2 * np.cos(u), 1.2 * np.sin(u), u]
            for u in np.linspace(-TAU, TAU, 100)  # 100 puntos en el rango [-TAU, TAU]
        ])
        curve2 = VMobject().set_points_as_corners(curve2_points).set_shade_in_3d(True)

        # Ejes
        axes = ThreeDAxes()

        # Configuración de cámara
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Animaciones
        self.play(Create(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()

class SurfacesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        # Definición de la esfera como una superficie parametrizada
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            u_range=[-PI / 2, PI / 2],
            v_range=[0, TAU],
            checkerboard_colors=[RED_D, RED_E],
            resolution=(20, 40)
        ).scale(2).set_shade_in_3d(True)  # Sombreado activado

        # Añadir los objetos a la escena
        self.add(axes)
        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(Write(sphere))
        self.wait()


class Text3D1(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Tex("This is a 3D text").scale(2).set_shade_in_3d(True)  # Sombreado activado
        text3d.rotate(PI / 2, axis=RIGHT)  # Rotarlo al eje deseado
        self.add(axes, text3d)
        self.wait()

class Text3D3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # Crear el texto 3D
        text3d = Text("This is a 3D text")
        self.add_fixed_in_frame_mobjects(text3d)  # Agregar el texto a la escena
        text3d.to_corner(UL)

        # Añadir los ejes a la escena
        self.add(axes)
        
        # Rotación continua de la cámara
        self.begin_ambient_camera_rotation()

        # Mostrar el texto
        self.play(Write(text3d))

        # Crear la esfera como una superficie paramétrica
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), 
            resolution=(15, 32)  # Resolucción de la superficie
        ).scale(2)  # Escalar la superficie

        # Animar la creación de la esfera (usando Create en lugar de ShowCreation)
        self.play(Create(sphere))
        self.wait(2)


class Text3D2(ThreeDScene):
    def construct(self):
        # Crear el sistema de ejes 3D
        axes = ThreeDAxes()

        # Configurar la cámara en una orientación específica
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Crear el texto en 3D y aplicarle escala
        text3d = Text("This is a 3D text").scale(2)

        # Rotar el texto en torno al eje X (RIGHT)
        text3d.rotate(PI/2, axis=RIGHT)

        # Añadir los objetos (ejes y texto) a la escena
        self.add(axes, text3d)

        # Comenzar la rotación ambiental de la cámara para visualizar la escena
        self.begin_ambient_camera_rotation(rate=0.1)

        # Esperar un momento para ver la escena
        self.wait(2)

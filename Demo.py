# %%manim -p Transform
from manim import *
from supplements import *

# Transformation, Curves (Beizier, B-spline, Monomial), Line Drawing


class Demo(Scene):
    def construct(self):
        casper = Casper()
        casper.scale(0.50)
        self.play(Create(casper))
        self.play(
            Rotate(casper, angle=2*PI, about_point=ORIGIN, rate_func=linear)
        )
        self.play(
            ScaleInPlace(casper, 2)
        )
        self.wait()


class RotateAxis(Scene):
    def construct(self):
        casper = Casper().scale(0.25)
        pos = np.array([3, 3, 0])
        casper.move_to(pos)
        ax = Axes().add_coordinates()
        plane = NumberPlane(x_range=(-10, 10, 1),
                            y_range=(-10, +10, 1),
                            x_length=10,
                            y_length=10)

        # self.play(Create(Casper))
        t = Tex("cos $\\theta$")
        m2 = Matrix([["cos\\theta", "sin\\theta"],
                     ["-sin\\theta", "cos\\theta"]])
        self.add(m2)
        # self.play(Rotate(ax, angle=PI/6, about_point=ORIGIN,
        #           rate_func=linear, run_time=3), Rotate(plane, angle=PI/6, about_point=ORIGIN,
        #           rate_func=linear, run_time=3))
        self.wait()

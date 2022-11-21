from manim import *


class Casper(VGroup):
    def __init__(self):
        super().__init__()
        circle1 = Circle(color=BLUE, fill_opacity=.95)
        circle2 = Circle(color=WHITE, fill_opacity=1)
        circle3 = Circle(color=WHITE, fill_opacity=1)
        square = Square()
        triangle = Triangle(color=LIGHT_BROWN, fill_opacity=1)
        triangle2 = Triangle()

        circle1.width = 2
        circle1.thickness = 3

        circle2.scale(0.2)
        circle2.set_stroke(width=1.25)
        circle2.shift(LEFT * .5)    

        circle3.scale(0.2)
        circle3.set_stroke(width=1.25)
        circle3.shift(RIGHT * .5)

        circle4 = Circle(color=BLACK, fill_opacity=.75)
        circle4.scale(0.155)
        circle4.set_stroke(width=1.25)
        circle4.shift(LEFT * .55)

        circle5 = Circle(color=BLACK, fill_opacity=.75)
        circle5.scale(0.155)
        circle5.set_stroke(width=1.25)
        circle5.shift(RIGHT * .45)

        square.shift(DOWN * 1.75)
        square.scale(.75)

        triangle.shift(UP * .65, RIGHT * .42)
        triangle.scale(.95)
        triangle.rotate(1.5)
        triangle.border = 2

        triangle2.shift(DOWN * 2)
        triangle2.rotate(PI)
        triangle2.scale(.45)

        smile = Arc(angle=.75*PI, radius=.2)
        smile.rotate(1.15*PI)
        smile.shift(DOWN * .65)

        a = [2, 0, 0]
        b = [0, 1.75, 0]
        c = [0, 0, 1.75]

        ap1 = ArcPolygon(a, b, c, radius=2, color=BLUE, fill_opacity=.75)

        ap_group = VGroup(ap1).arrange()
        ap_group.shift(DOWN * 1.75)
        ap_group.rotate(1.65 * PI * .75)

        self.add(ap_group, triangle2, circle1, circle2,
                 circle3, circle4, circle5, triangle, smile)


class transformer(Scene):

    def construct(self):
        s = Casper()
        s.scale(.5)
        ttext = Text("Translation")
        ttext.shift(UP*3)

        self.play(Create(s))
        self.play(Write(ttext))
        self.play(s.animate.shift(RIGHT*4))
        self.play(s.animate.shift(LEFT*4))
        self.wait(4)
        self.remove(ttext)
        ttext = Text("Scaling")
        ttext.shift(UP*3)
        self.play(Write(ttext))

        self.play(s.animate.scale(2))
        self.wait(4)
        self.remove(ttext)

        ttext = Text("Rotation")
        ttext.shift(UP*3)
        self.play(Write(ttext))
        self.play(Rotate(s, angle=PI, about_point=ORIGIN, run_time=2))
        self.wait(4)
        self.remove(ttext)
        self.play(Uncreate(s))
        self.wait(2)
        st = Text("Old Coordinate: x, y", font_size=25)
        st.shift(UP*2, LEFT*3)
        self.play(Write(st))
        st2 = Text("New Coordinate: x', y'", font_size=25)
        st2.shift(UP*1, LEFT*3)
        self.play(Write(st2))
        st3 = Text(
            "In That Case:\n\nx'= Scaling * x\n\ny'=Scaling * y", font_size=25)
        st3.shift(UP*-2, LEFT*3)

        ax = Axes().add_coordinates()
        dot_axes = Dot(ax.coords_to_point(5, 2), color=GREEN)
        lines = ax.get_lines_to_point(ax.c2p(5, 2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        plane = NumberPlane()
        dot_scene = Dot((0, 0, 0), color=RED)
        g = Group(dot_scene, ax, dot_axes, lines)
        self.add(g)
        c = Casper()
        c.scale(.5)
        c.shift(UP*2.25, RIGHT*2.25)
        self.add(c)
        self.wait(3)
        self.remove(c)
        self.play(c.animate.scale(1.75))
        self.play(Write(st3))
        self.wait(3)
        self.remove(st, st2, g)
        self.play(st3.animate.to_edge(UP))
        # self.add(number_plane)
        m0 = Matrix([['X'], ['Y']])
        m1 = Matrix([['x'], ['y']])
        m2 = Matrix([['Sx', 0], [0, 'Sy']])
        self.add(m0)
        self.play(m0.animate.to_edge(LEFT))
        self.add(m1)
        self.play(m1.animate.to_edge(LEFT-2))
        self.add(m2)
        self.play(m2.animate.to_edge(DOWN * 2))
        self.remove(m1)
        self.remove(m2)
        self.wait(3)
        g = Group(
            m1, m2
        ).arrange_in_grid(buff=0.5)
        self.add(g)

        self.wait(2)
        self.play(g.animate.to_edge(LEFT))
        self.wait(3)
        self.remove(c, st3, g, m0)
        self.wait(3)
        self.add(c)
        c.scale(0.5)
        self.play(

            Rotate(
                c,
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
        )
        self.remove(c)
        self.wait(2)
        cp = Casper()
        cp.shift(RIGHT*3, DOWN * 2)
        cp.scale(.6)
        self.add(cp)
        self.wait(4)

        quote = Text(
            "\"WHY ARE YOU MAKING ME ROTATE LIKE THIS?\"\n-Casper", font_size=25)
        self.play(Write(quote))
        self.wait(5)
        self.remove(cp, quote)

        st = Text("Old Coordinate: x, y", font_size=25)
        st.shift(UP*2, LEFT*3)
        self.play(Write(st))
        st2 = Text("New Coordinate: X, Y", font_size=25)
        st2.shift(UP*1, LEFT*3)
        self.play(Write(st2))
        st3 = Text(
            "In That Case:\n\nX= x cos \\theta - y sin \\theta\n\nY=x sin \\theta + y cos \\theta", font_size=25)
        st3.shift(UP*-2, LEFT*3)

        self.wait(3)
        ax = Axes().add_coordinates()
        dot_axes = Dot(ax.coords_to_point(2, 2), color=GREEN)
        lines = ax.get_lines_to_point(ax.c2p(2, 2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        plane = NumberPlane()
        dot_scene = Dot((0, 0, 0), color=RED)
        g = Group(dot_scene, ax, dot_axes, lines)
        self.add(g)
        arrow = Arrow(np.array([0, 0, 0]), np.array([2, 2, 0]))
        self.play(GrowArrow(arrow))
        theta = Text("\\theta = 45 ° ")
        self.wait(2)
        arrow1 = Arrow(np.array([0, 0, 0]), np.array([2, 0, 0]))
        self.play(GrowArrow(arrow1))
        arrow2 = Arrow(np.array([2, 0, 0]), np.array([2, 2, 0]))
        self.play(GrowArrow(arrow2))
        self.play(Write(st3))
        self.wait(4)
        self.remove(g, st, st2, arrow1, arrow2, arrow)
        self.play(st3.animate.to_edge(UP))
        # self.add(number_plane)
        m0 = Matrix([['X'], ['Y']])
        m1 = Matrix([['x'], ['y']])
        m2 = Matrix([["cos\\theta", "sin\\theta"],
                    ["-sin\\theta", "cos\\theta"]])
        self.add(m0)
        self.play(m0.animate.to_edge(LEFT))
        self.add(m1)
        self.play(m1.animate.to_edge(LEFT-2))
        self.add(m2)
        self.play(m2.animate.to_edge(DOWN * 2))
        self.remove(m1)
        self.remove(m2)
        self.wait(3)
        g = Group(
            m1, m2
        ).arrange_in_grid(buff=0.5)
        self.add(g)

        self.wait(2)
        self.play(g.animate.to_edge(LEFT))
        self.wait(3)
        self.remove(c, st3, g, m0)
        self.wait(3)

        m0 = Matrix([['0'], ['0']])
        m1 = Matrix([[0], [0]])
        m2 = Matrix([["a", "b"], ["c", "d"]])
        self.add(m0)
        self.play(m0.animate.to_edge(LEFT))
        self.add(m1)
        self.play(m1.animate.to_edge(LEFT-2))
        self.add(m2)
        g = Group(
            m2, m1
        ).arrange_in_grid(buff=0.5)
        self.play(g.animate.to_edge(UP))
        self.play(m0.animate.to_edge(UP+.25))
        self.wait(3)
        tr = Text("Translation", font_size=35)
        self.play(Write(tr))
        cross = Cross()
        cross.shift(DOWN*2)
        self.add(cross)
        self.wait(3)
        self.remove(g, m0, cross, tr)
        self.wait(3)
        affine = Text("Homogenuse Coordinates", font_size=35)
        self.play(Write(affine))
        self.wait(3)
        affine1 = Text("1.Helps in Matrix Composition", font_size=25)
        self.play(Write(affine1))
        affine1.shift(DOWN*2)
        self.wait(3)
        affine2 = Text(
            "2.Add an additional dimension to calculate translation matrix", font_size=25)
        self.play(Write(affine2))
        affine2.shift(DOWN*3)
        self.wait(3)
        self.remove(affine, affine1, affine2)
        self.wait(3)
        st = Text("Old Coordinate: x, y", font_size=20)
        st.shift(UP*2, LEFT*3)
        self.play(Write(st))
        st2 = Text("New Coordinate: x', y'", font_size=20)
        st2.shift(UP*1, LEFT*3)
        self.play(Write(st2))
        st3 = Text("In That Case:\n\nx'= Tx + x\n\ny'=Ty + y", font_size=25)
        st3.shift(UP*-2, LEFT*3)

        ax = Axes().add_coordinates()
        dot_axes = Dot(ax.coords_to_point(5, 2), color=GREEN)
        lines = ax.get_lines_to_point(ax.c2p(5, 2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        plane = NumberPlane()
        dot_scene = Dot((0, 0, 0), color=RED)
        g = Group(dot_scene, ax, dot_axes, lines)
        self.add(g)
        c = Casper()
        c.scale(.5)
        c.shift(UP*2.25, RIGHT*2.25)
        self.add(c)
        self.wait(3)
        self.remove(c)
        self.play(c.animate.shift(RIGHT))
        self.play(Write(st3))
        self.wait(3)
        self.remove(st, st2, g)
        self.play(st3.animate.to_edge(UP))
        # self.add(number_plane)
        m0 = Matrix([['X'], ['Y'], [1]])
        m1 = Matrix([['x'], ['y'], [1]])
        m2 = Matrix([[0, 0, 'Tx'], [0, 0, 'Ty']])
        self.add(m0)
        self.play(m0.animate.to_edge(LEFT))
        self.add(m1)
        self.play(m1.animate.to_edge(LEFT-2))
        self.add(m2)
        self.play(m2.animate.to_edge(DOWN * 2))
        self.remove(m1)
        self.remove(m2)
        self.wait(3)
        g = Group(
            m1, m2
        ).arrange_in_grid(buff=0.5)
        self.add(g)

        self.wait(2)
        self.play(g.animate.to_edge(LEFT))
        self.wait(3)
        self.remove(c, st3, g, m0)
        self.wait(3)

        self.wait(5)

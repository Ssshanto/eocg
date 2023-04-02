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


class RWQuote(Scene):
    def construct(self):

        subtitle = Text("Computer graphics is so pervasive around us in movies, computer games...").move_to(
            ORIGIN + 3 * DOWN).scale(0.4)

        self.add(subtitle)
        rw_quote = Tex(
            r"I play a lot of computer games. I love computer graphics. I’ve had Pixar in me for a long time.")
        rw = Tex("- Robin Williams").next_to(rw_quote,
                                             DOWN/4)
        title = Tex("Comedian, Actor, Video Game Enthusiast").next_to(
            rw, DOWN/4).set_color(ORANGE)
        rw_quote.scale(0.7)
        rw.scale(0.7)
        title.scale(0.6)

        self.play(Write(rw_quote), run_time=4)

        self.play(Write(rw), run_time=1)
        self.play(Write(title), run_time=2)
        self.wait(2)
        self.remove(subtitle)
        subtitle = Text("and even in this video...").move_to(
            ORIGIN + 3 * DOWN).scale(0.4)
        self.add(subtitle)
        self.wait(4)
        self.remove(subtitle)
        subtitle = Text("Almost to the point where we don't even think to ask the question 'How?'").move_to(
            ORIGIN + 3 * DOWN).scale(0.4)
        self.add(subtitle)
        self.wait(3)
        self.clear()


class CasperMove(Scene):
    def construct(self):
        subtitle = Text("Let's take this simple scene of Casper the friendly ghost wandering around for example").move_to(
            ORIGIN + 3 * DOWN).scale(0.4)
        self.add(subtitle)
        casper = Casper().scale(0.5)
        self.play(Create(casper))
        self.wait(1)

        self.play(casper.animate.shift(3 * LEFT), run_time=3)
        self.play(Rotate(casper, angle=PI/12, about_point=ORIGIN))
        self.remove(subtitle)
        subtitle = Text("How is the action of movement and rotation mimicked in this flip-book like manner?").move_to(
            ORIGIN + 3 * DOWN).scale(0.4)
        self.add(subtitle)
        self.play(casper.animate.shift(6 * RIGHT), run_time=3)
        self.wait(2)

        circle1 = Circle(color=BLUE, fill_opacity=.95)
        circle1.width = 2
        circle1.thickness = 3
        circle1.move_to(ORIGIN + RIGHT)
        circle1.scale(.5)

        triangle = Triangle(color=LIGHT_BROWN, fill_opacity=1)
        triangle.scale(.5)
        triangle.rotate(PI/6, about_point=ORIGIN)
        triangle.border = 2
        triangle.move_to(ORIGIN + LEFT)

        subtitle = Text("On an even more rudimentary level, how are these geometric shapes that Casper consists of drawn?").move_to(
            ORIGIN + 3 * DOWN).scale(0.4)

        self.clear()
        self.add(subtitle)
        self.play(Create(triangle), Create(circle1))
        self.wait(2)


class CurvesDraw(Scene):
    def construct(self):
        p0 = np.array([-3.5, -1, 0])  # startpoint
        p1 = np.array([-3, 2, 0])  # 1st point
        p2 = np.array([3, 2, 0])  # 2nd point
        p3 = np.array([3.5, -1, 0])  # 3rd point

        d0 = Dot(point=p0).set_color(BLUE)
        d1 = Dot(point=p1).set_color(GREEN)
        d2 = Dot(point=p2).set_color(GREEN)
        d3 = Dot(point=p3).set_color(BLUE)

        l1 = Line(d0, d1).set_opacity(0.5)
        l2 = Line(d1, d2).set_opacity(0.5)
        l3 = Line(d2, d3).set_opacity(0.5)

        subtitle = Text("How do we represent the curves that make up these shapes geometrically?").move_to(
            ORIGIN + 3 * DOWN).scale(0.4)
        self.add(subtitle)
        self.play(Create(d0), Create(d1), Create(d2), Create(
            d3), Create(l1), Create(l2), Create(l3))

        bezier = CubicBezier(p0, p1, p2, p3).set_color(ORANGE)
        self.play(Create(bezier, run_time=3))
        self.wait(2)
        self.remove(subtitle)

        subtitle = Text("How do we ensure that the artist can freely manipulate these curves to create beautiful shapes?").move_to(
            ORIGIN + 3 * DOWN).scale(0.4)
        self.add(subtitle)
        self.wait()

        p1 = p1 + 2 * LEFT + 1 * DOWN
        p2 = p2 + 3 * LEFT + UP
        dn1 = Dot(point=p1).set_color(GREEN)
        dn2 = Dot(point=p2).set_color(GREEN)

        l1n = Line(p0, p1).set_opacity(0.5)
        l2n = Line(p1, p2).set_opacity(0.5)
        l3n = Line(p2, p3).set_opacity(0.5)

        newBezier = CubicBezier(p0, p1, p2, p3).set_color(ORANGE)

        self.play(Transform(d1, dn1), Transform(d2, dn2), Transform(
            l1, l1n), Transform(l2, l2n), Transform(l3, l3n), Transform(bezier, newBezier))

        self.wait(2)
        self.remove(d1, d2, l1, l2, l3, bezier)

        p1 = p1 + 3 * RIGHT + UP
        p2 = p2 + 3 * LEFT
        dnn1 = Dot(point=p1).set_color(GREEN)
        dnn2 = Dot(point=p2).set_color(GREEN)

        l1nn = Line(p0, p1).set_opacity(0.5)
        l2nn = Line(p1, p2).set_opacity(0.5)
        l3nn = Line(p2, p3).set_opacity(0.5)

        newBezier2 = CubicBezier(p0, p1, p2, p3).set_color(ORANGE)

        self.play(Transform(dn1, dnn1), Transform(dn2, dnn2), Transform(
            l1n, l1nn), Transform(l2n, l2nn), Transform(l3n, l3nn), Transform(newBezier, newBezier2))

        self.wait(2)


class LineDraw(Scene):
    def construct(self):
        subtitle = Text("Even for a basic shape like a line...").move_to(
            ORIGIN + 2.5 * DOWN).scale(0.4)

        self.add(subtitle)
        p1 = np.array([-2, -2, 0])
        p2 = np.array([2, 2, 0])

        l1 = Line(p1, p2).set_color(ORANGE)
        self.play(Create(l1))
        self.wait()

        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )

        self.play(Create(number_plane, run_time=3))
        self.remove(subtitle)
        subtitle = Text("...How do we determine which pixels of the display should light up to draw the line?").move_to(
            ORIGIN + 2.5 * DOWN).scale(0.4)
        self.wait(2)
        self.add(subtitle)
        self.wait()

        start_coord = p1 + 0.5 * UP + 0.5 * RIGHT
        r1 = Rectangle(width=1, height=1).move_to(
            start_coord).set_color(ORANGE).set_opacity(0.5)
        r2 = Rectangle(width=1, height=1).move_to(
            start_coord + UP + RIGHT).set_color(ORANGE).set_opacity(0.5)
        r3 = Rectangle(width=1, height=1).move_to(
            start_coord + 2 * UP + 2 * RIGHT).set_color(ORANGE).set_opacity(0.5)
        r4 = Rectangle(width=1, height=1).move_to(
            start_coord + 3 * UP + 3 * RIGHT).set_color(ORANGE).set_opacity(0.5)

        self.play(Create(r1, run_time=0.3))
        self.play(Create(r2, run_time=0.3))
        self.play(Create(r3, run_time=0.3))
        self.play(Create(r4, run_time=0.3))
        self.wait(2)


class eocg(Scene):
    def construct(self):
        subtitle = Text("Pursuing the building blocks of image generation leads us to this underappreciated yet elegant domain").move_to(
            ORIGIN + 2.5 * DOWN).scale(0.4)
        self.add(subtitle)
        self.wait(4)
        self.remove(subtitle)

        subtitle = Text("This is, The Essence of Computer Graphics").move_to(
            ORIGIN + 2.5 * DOWN).scale(0.4)
        titleTop = Tex("The Essence of").move_to(ORIGIN + 0.75 * UP)
        titleBottom = Tex("Computer Graphics").move_to(
            ORIGIN).set_color(ORANGE).scale(2)
        self.add(subtitle)
        self.play(Write(titleTop), Write(titleBottom))
        self.wait(5)

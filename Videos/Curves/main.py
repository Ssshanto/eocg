from manim import *


def lerp(p0, p1, t):
    return (1 - t) * p0 + t * p1


class ParametricDefinition(Scene):
    def construct(self):
        # Let's denote two points P0 and P1
        p0 = np.array([-3.5, -1, 0])  # startpoint
        p1 = np.array([3.5, 1, 0])  # endpoint

        d0 = Dot(point=p0).set_color(PINK)
        d1 = Dot(point=p1).set_color(PINK)
        p0_label = Tex(r"$ P_{0} $").next_to(d0, DOWN)
        p1_label = Tex(r"$ P_{1} $").next_to(d1, DOWN)

        l1 = Line(d0, d1)

        self.play(Create(d0), Create(d1))
        self.play(Write(p0_label), Write(p1_label))
        self.play(Create(l1))
        self.wait()

        # We can define any point on the line as a parametric function P(t) = (1 - t) * p0 + t * p1. Values of t between 0 and 1 specify any point on the line.
        # this is known as lerp(P0, P1, t)
        # Show parametric function

        parametric_formula = MathTex(r"P(t) = (1 - t)P_{0} + tP_{1}")
        parametric_formula.move_to(ORIGIN + 3 * DOWN)
        self.play(Write(parametric_formula))
        self.wait()

        demo_tvalues = [0.5, 0.2, 0.7]
        old_line = Line(d0, d0).set_color(BLUE)
        for t in demo_tvalues:
            endpoint = lerp(p0, p1, t)
            new_line = Line(d0, endpoint).set_color(BLUE).set_stroke(width=5)
            enddot = Dot(point=endpoint).set_color(BLUE)
            t_val_text = Variable(
                t, label="t", num_decimal_places=1)
            t_val_text.next_to(endpoint, DOWN)
            t_val_text.set_color(BLUE)
            t_val_text.scale(0.75)
            self.play(Transform(old_line, new_line),
                      Write(t_val_text), Create(enddot))
            self.wait()
            self.remove(t_val_text)
            self.remove(enddot)
            # self.remove(old_line)
            # old_line = new_line
            # Show t labels

        self.clear()
        self.add(d0, p0_label, l1)
        p1 = np.array([0, 2, 0])  # 2nd point
        p2 = np.array([3.5, -1, 0])

        d1 = Dot(point=p1).set_color(PINK)
        d2 = Dot(point=p2).set_color(PINK)
        p1_label = Tex(r"$ P_{1} $").next_to(d1, RIGHT)
        p2_label = Tex(r"$ P_{2} $").next_to(d2, DOWN)
        new_line = Line(d0, d1)
        l2 = Line(d1, d2)

        self.add(d1)
        self.play(Transform(l1, new_line))
        self.play(Create(d2), Create(l2), Write(p1_label), Write(p2_label))
        self.wait()


class QuadraticBezierSetup(Scene):
    def construct(self):
        p0 = np.array([-3.5, -1, 0])  # startpoint
        p1 = np.array([0, 2, 0])  # 2nd point
        p2 = np.array([3.5, -1, 0])  # 3rd point

        d0 = Dot(point=p0).set_color(PINK)
        d1 = Dot(point=p1).set_color(PINK)
        d2 = Dot(point=p2).set_color(PINK)
        p0_label = Tex(r"$ P_{0} $").next_to(d0, DOWN)
        p1_label = Tex(r"$ P_{1} $").next_to(d1, RIGHT)
        p2_label = Tex(r"$ P_{2} $").next_to(d2, DOWN)
        l1 = Line(d0, d1)
        l2 = Line(d1, d2)

        self.add(d0, d1, d2, p0_label, p1_label, p2_label, l1, l2)

        demo_tvalues = [0.5, 0.2, 0.7]
        old_line1 = Line(d0, d0).set_color(BLUE)
        old_line2 = Line(d1, d1).set_color(BLUE)
        for t in demo_tvalues:
            endpoint1 = lerp(p0, p1, t)
            endpoint2 = lerp(p1, p2, t)
            new_line1 = Line(d0, endpoint1).set_color(
                BLUE).set_stroke(width=5)
            new_line2 = Line(d1, endpoint2).set_color(
                BLUE).set_stroke(width=5)
            enddot1 = Dot(point=endpoint1).set_color(BLUE)
            enddot2 = Dot(point=endpoint2).set_color(BLUE)

            t_val_text1 = Variable(
                t, label="t", num_decimal_places=1)
            t_val_text1.next_to(endpoint1, RIGHT)
            t_val_text1.set_color(BLUE)
            t_val_text1.scale(0.75)

            t_val_text2 = Variable(
                t, label="t", num_decimal_places=1)
            t_val_text2.next_to(endpoint2, RIGHT)
            t_val_text2.set_color(BLUE)
            t_val_text2.scale(0.75)

            self.play(Transform(old_line1, new_line1), Write(t_val_text1), Write(t_val_text2),
                      Transform(old_line2, new_line2))
            self.wait()
            self.remove(enddot1, enddot2, t_val_text1, t_val_text2)

        self.wait()
        # We add another line that connects these two parametric points


class QuadraticBezierDraw(Scene):
    def construct(self):
        p0 = np.array([-3.5, -1, 0])  # startpoint
        p1 = np.array([0, 2, 0])  # 2nd point
        p2 = np.array([3.5, -1, 0])  # 3rd point

        d0 = Dot(point=p0).set_color(PINK)
        d1 = Dot(point=p1).set_color(PINK)
        d2 = Dot(point=p2).set_color(PINK)
        p0_label = Tex(r"$ P_{0} $").next_to(d0, DOWN)
        p1_label = Tex(r"$ P_{1} $").next_to(d1, RIGHT)
        p2_label = Tex(r"$ P_{2} $").next_to(d2, DOWN)
        l1 = Line(d0, d1)
        l2 = Line(d1, d2)
        dt1 = Dot(point=p0).set_color(BLUE)
        dt2 = Dot(point=p1).set_color(BLUE)
        self.add(l1, l2, d0, d1, d2, p0_label, p1_label, p2_label)

        t = 0
        old_dt1 = Dot(point=lerp(p0, p1, 0.5)).set_color(BLUE)
        old_dt2 = Dot(point=lerp(p1, p2, 0.5)).set_color(BLUE)
        old_midline = Line(lerp(p0, p1, 0.5), lerp(
            p1, p2, 0.5)).set_opacity(0.5)
        old_dt3 = Dot(point=lerp(lerp(p0, p1, 0.5), lerp(
            p1, p2, 0.5), 0.5)).set_color(ORANGE)

        dt1_label = Tex(r"$ t = 0.5 $").next_to(old_dt1, LEFT).set_color(BLUE)
        dt2_label = Tex(r"$ t = 0.5 $").next_to(old_dt2, RIGHT).set_color(BLUE)
        dt3_label = Tex(r"$ t = 0.5 $").next_to(
            old_dt3, DOWN).set_color(ORANGE)

        self.play(Create(old_midline))
        self.play(Create(old_dt1), Create(old_dt2))
        self.play(Write(dt1_label), Write(dt2_label))
        self.play(Create(old_dt3))
        self.play(Write(dt3_label))

        self.wait(2)
        self.remove(old_dt1, old_dt2, old_dt3, dt1_label, dt2_label, dt3_label)
        old_curve_point = p0
        epsilon = 0.025
        first = True

        while t < 1 + epsilon:
            pt1 = lerp(p0, p1, t)
            pt2 = lerp(p1, p2, t)
            new_midline = Line(pt1, pt2).set_opacity(0.25)
            pt3 = lerp(pt1, pt2, t)

            new_dt1 = Dot(point=pt1).set_color(BLUE)
            new_dt2 = Dot(point=pt2).set_color(BLUE)
            new_dt3 = Dot(point=pt3).set_color(ORANGE)

            anim_runtime = 0.05
            new_curve = CubicBezier(
                old_curve_point, old_curve_point, pt3, pt3).set_color(ORANGE)

            if first:
                self.play(Transform(old_dt1, new_dt1), Transform(old_dt2, new_dt2),
                          Transform(old_midline, new_midline), Transform(old_dt3, new_dt3))
                first = False

            self.play(Transform(old_dt1, new_dt1, run_time=anim_runtime), Transform(old_dt2, new_dt2, run_time=anim_runtime),
                      Transform(old_midline, new_midline, run_time=anim_runtime), Transform(old_dt3, new_dt3, run_time=anim_runtime), Create(new_curve, run_time=anim_runtime))
            t += 0.025
            old_curve_point = pt3
            # points = [p0, p1, p2]
            # demo_bezier = bezier(points)

        self.wait(2)
        quadratic_bezier_label = Text("Qaudratic Bezier Curve").move_to(
            ORIGIN + 3 * DOWN).set_color(ORANGE)
        self.play(Write(quadratic_bezier_label))
        self.wait(2)
        self.clear()

        self.add(l1, l2, d0, d2, p0_label, p2_label)

        p1 = np.array([-3, 2, 0])  # 2nd point
        p2 = np.array([3.5, -1, 0])  # 4th point
        p3 = np.array([3, 2, 0])  # 3rd point

        new_d1 = Dot(point=p1).set_color(PINK)
        new_d2 = Dot(point=p3).set_color(PINK)
        new_l1 = Line(p0, p1)
        new_l2 = Line(p1, p3)
        new_l3 = Line(p3, p2)

        new_p1_label = Tex(r"$ P_{1} $").next_to(new_d1, LEFT)
        new_p2_label = Tex(r"$ P_{2} $").next_to(new_d2, RIGHT)
        changed_p2_label = Tex(r"$ P_{3} $").next_to(d2, DOWN)

        self.play(Transform(l1, new_l1), Transform(l2, new_l3),
                  Create(new_l2), Transform(d1, new_d1), Create(new_d2), Transform(p2_label, changed_p2_label), Write(new_p1_label), Write(new_p2_label))
        self.wait(2)


def drawCubicBezier(scene_obj, p0, p1, p2, p3, drawNew):

    old_midline1 = Line(p0, p1).set_opacity(0.25)
    old_midline2 = Line(p1, p2).set_opacity(0.25)
    old_dm1 = Dot(p0).set_color(BLUE)
    old_dm2 = Dot(p1).set_color(BLUE)
    old_dm3 = Dot(p2).set_color(BLUE)

    old_midline = Line(p0, p1)
    old_dmstart = Dot(p0).set_color(GREEN).set_opacity(0.5)
    old_dmend = Dot(p1).set_color(GREEN).set_opacity(0.5)
    old_dm = Dot(point=p0).set_color(ORANGE)

    if drawNew == True:
        d0 = Dot(p0).set_color(PINK)
        d1 = Dot(p1).set_color(RED)
        d2 = Dot(p2).set_color(PINK)
        d3 = Dot(p3).set_color(RED)
        l1 = Line(p0, p1).set_opacity(0.5)
        l2 = Line(p1, p2).set_opacity(0.5)
        l3 = Line(p2, p3).set_opacity(0.5)
        scene_obj.play(Create(l1), Create(l2), Create(l3), Create(
            d0), Create(d1), Create(d2), Create(d3))

    t = 0
    old_curve_point = p0
    epsilon = 0.025
    anim_runtime = 0.05

    while t <= 1 + epsilon:
        pt1 = lerp(p0, p1, t)
        pt2 = lerp(p1, p2, t)
        pt3 = lerp(p2, p3, t)
        new_midline1 = Line(pt1, pt2).set_opacity(0.25)
        new_midline2 = Line(pt2, pt3).set_opacity(0.25)

        new_dm1 = Dot(pt1).set_color(BLUE)
        new_dm2 = Dot(pt2).set_color(BLUE)
        new_dm3 = Dot(pt3).set_color(BLUE)

        ptm1 = lerp(pt1, pt2, t)
        ptm2 = lerp(pt2, pt3, t)
        pm = lerp(ptm1, ptm2, t)
        new_midline = Line(ptm1, ptm2)

        new_dmstart = Dot(ptm1).set_color(GREEN).set_opacity(0.5)
        new_dmend = Dot(ptm2).set_color(GREEN).set_opacity(0.5)
        new_dm = Dot(point=pm).set_color(ORANGE)

        new_curve = CubicBezier(
            old_curve_point, old_curve_point, pm, pm).set_color(ORANGE)

        scene_obj.play(Transform(old_midline1, new_midline1, run_time=anim_runtime), Transform(old_midline2, new_midline2, run_time=anim_runtime), Transform(
            old_dm1, new_dm1, run_time=anim_runtime), Transform(old_dm2, new_dm2, run_time=anim_runtime), Transform(old_dm3, new_dm3, run_time=anim_runtime), Transform(old_midline, new_midline, run_time=anim_runtime), Transform(old_dmstart, new_dmstart, run_time=anim_runtime), Transform(old_dmend, new_dmend, run_time=anim_runtime), Transform(old_dm, new_dm, run_time=anim_runtime), Create(new_curve, run_time=anim_runtime))

        t += epsilon
        old_curve_point = pm
        # points = [p0, p1, p2]
        # demo_bezier = bezier(points)

    if not drawNew:
        scene_obj.wait()
        cubic_bezier_label = Text("Cubic Bezier Curve").move_to(
            ORIGIN + 3 * DOWN).set_color(ORANGE)
        scene_obj.play(Write(cubic_bezier_label))

    scene_obj.wait(2)
    scene_obj.clear()


class CubicBezierDraw(Scene):
    def construct(self):
        p0 = np.array([-3.5, -1, 0])  # startpoint
        p1 = np.array([-3, 2, 0])  # 1st point
        p2 = np.array([3, 2, 0])  # 2nd point
        p3 = np.array([3.5, -1, 0])  # 3rd point

        d0 = Dot(point=p0).set_color(PINK)
        d1 = Dot(point=p1).set_color(RED)
        d2 = Dot(point=p2).set_color(RED)
        d3 = Dot(point=p3).set_color(PINK)
        p0_label = Tex(r"$ P_{0} $").next_to(d0, DOWN)
        p1_label = Tex(r"$ P_{1} $").next_to(d1, LEFT)
        p2_label = Tex(r"$ P_{2} $").next_to(d2, RIGHT)
        p3_label = Tex(r"$ P_{3} $").next_to(d3, DOWN)

        l1 = Line(d0, d1).set_opacity(0.5)
        l2 = Line(d1, d2).set_opacity(0.5)
        l3 = Line(d2, d3).set_opacity(0.5)

        self.add(l1, l2, l3, d0, d1, d2, d3, p0_label, p1_label,
                 p2_label, p3_label)
        self.wait(2)

        midline1 = Line(lerp(p0, p1, 0.5), lerp(p1, p2, 0.5)).set_opacity(0.75)
        midline2 = Line(lerp(p1, p2, 0.5), lerp(p2, p3, 0.5)).set_opacity(0.75)
        dm1 = Dot(point=lerp(p0, p1, 0.5)).set_color(BLUE)
        dm2 = Dot(point=lerp(p1, p2, 0.5)).set_color(BLUE)
        dm3 = Dot(point=lerp(p2, p3, 0.5)).set_color(BLUE)

        ldm1 = Tex(r"$ t = 0.5 $").next_to(
            dm1, LEFT).set_color(BLUE).scale(0.75)
        ldm2 = Tex(r"$ t = 0.5 $").next_to(
            dm2, UP).set_color(BLUE).scale(0.75)
        ldm3 = Tex(r"$ t = 0.5 $").next_to(
            dm3, RIGHT).set_color(BLUE).scale(0.75)

        self.play(Create(midline1), Create(midline2),
                  Create(dm1), Create(dm2), Create(dm3), Write(ldm1), Write(ldm2), Write(ldm3))
        self.wait(2)

        midline = Line(midline1.get_center(), midline2.get_center())
        dmstart = Dot(point=midline1.get_center()).set_color(GREEN)
        ldmstart = Tex(r"$ t = 0.5 $").next_to(
            dmstart, LEFT).set_color(GREEN).scale(0.75)
        dmend = Dot(point=midline2.get_center()).set_color(GREEN)
        ldmend = Tex(r"$ t = 0.5 $").next_to(
            dmend, RIGHT).set_color(GREEN).scale(0.75)
        dm = Dot(point=lerp(midline1.get_center(),
                            midline2.get_center(), 0.5)).set_color(ORANGE)

        ldm = Tex(r"$ t = 0.5 $").next_to(
            dm, DOWN).set_color(ORANGE)

        self.play(Create(dmstart), Create(dmend),
                  Write(ldmstart), Write(ldmend), Create(midline), Create(dm), Write(ldm))

        self.wait()
        self.remove(dm1, dm2, dm3, ldm1, ldm2, ldm3, ldm, ldmstart, ldmend)
        new_midline1 = Line(p0, p1).set_opacity(0.25)
        new_midline2 = Line(p1, p2).set_opacity(0.25)
        new_dm1 = Dot(p0).set_color(BLUE)
        new_dm2 = Dot(p1).set_color(BLUE)
        new_dm3 = Dot(p2).set_color(BLUE)

        new_midline = Line(p0, p0)
        new_dmstart = Dot(p0).set_color(GREEN).set_opacity(0.5)
        new_dmend = Dot(p1).set_color(GREEN)
        new_dm = Dot(point=p0).set_color(ORANGE)

        self.play(Transform(midline1, new_midline1), Transform(midline2, new_midline2), Transform(
            dm1, new_dm1), Transform(dm2, new_dm2), Transform(dm3, new_dm3), Transform(midline, new_midline), Transform(dmstart, new_dmstart), Transform(dmend, new_dmend), Transform(dm, new_dm))
        self.wait()

        drawCubicBezier(self, p0, p1, p2, p3, False)
        p0 = np.array([1.5, 3.5, 0])  # startpoint
        p1 = np.array([-3.5, -2, 0])  # 1st point
        p2 = np.array([3, 3, 0])  # 2nd point
        p3 = np.array([-2.5, -3, 0])  # 3rd point
        drawCubicBezier(self, p0, p1, p2, p3, True)
        self.wait()

        p0 = np.array([1, 3, 0])  # startpoint
        p1 = np.array([2.5, 2, 0])  # 1st point
        p2 = np.array([-5, -3, 0])  # 2nd point
        p3 = np.array([-2, -2.5, 0])  # 3rd point
        drawCubicBezier(self, p0, p1, p2, p3, True)


# class BezierSplineExample(Scene):
#     def construct(self):
#         p0 = np.array([-3.5, -1, 0])  # startpoint
#         p3 = np.array([3.5, -1, 0])  # endpoint
#         p1 = p0 + 1 * RIGHT + 3 * UP  # handle 1
#         p2 = p3 - 1 * RIGHT + 3 * UP  # handle 2

#         d0 = Dot(point=p0).set_color(BLUE)
#         d3 = Dot(point=p3).set_color(BLUE)
#         d1 = Dot(point=p1).set_color(RED)
#         d2 = Dot(point=p2).set_color(RED)

#         l1 = Line(p0, p1)
#         l2 = Line(p1, p2)
#         l3 = Line(p2, p3)
#         l1.set_opacity(.25)
#         l2.set_opacity(.25)
#         l3.set_opacity(.25)

#         self.add(d0, d1, d2, d3)
#         self.play(Create(l1))
#         self.play(Create(l2))
#         self.play(Create(l3))

#         self.add(d0, d1, d2, d3)
#         self.add(l1, l2, l3)

#         bezier = CubicBezier(p0, p1, p2, p3)
#         self.play(Create(bezier))
#         self.wait()

#         # for i in range(10):
#         #     self.remove(d1, d2, l1, l2, l3, bezier)

#         #     p1 = p1 - 0.1 * RIGHT
#         #     bezier = CubicBezier(p0, p1, p2, p3)

#         #     l1 = Line(p0, p1)
#         #     l2 = Line(p1, p2)
#         #     l3 = Line(p2, p3)
#         #     l1.set_opacity(.25)
#         #     l2.set_opacity(.25)
#         #     l3.set_opacity(.25)

#         #     d1 = Dot(point=p1).set_color(RED)
#         #     d2 = Dot(point=p2).set_color(RED)

#         #     self.add(d1, d2, l1, l2, l3)
#         #     self.add(bezier)
#         #     self.wait(0.1)
#         #     self.remove(bezier)
#         #     # self.remove(bezier)
#         #     # self.remove(d1, d2)

#         # for i in range(10):
#         #     self.remove(d1, d2, l1, l2, l3, bezier)

#         #     p2 = p2 + 0.1 * RIGHT
#         #     bezier = CubicBezier(p0, p1, p2, p3)

#         #     l1 = Line(p0, p1)
#         #     l2 = Line(p1, p2)
#         #     l3 = Line(p2, p3)
#         #     l1.set_opacity(.25)
#         #     l2.set_opacity(.25)
#         #     l3.set_opacity(.25)

#         #     d1 = Dot(point=p1).set_color(RED)
#         #     d2 = Dot(point=p2).set_color(RED)

#         #     self.add(d1, d2, l1, l2, l3)
#         #     self.add(bezier)
#         #     self.wait(0.1)
#         #     self.remove(bezier)
#         #     # self.remove(bezier)
#         #     # self.remove(d1, d2)

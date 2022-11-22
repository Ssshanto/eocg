from manim import *
import math


class naive(MovingCameraScene):
    def construct(self):
        x1 = 2
        y1 = 3
        x2 = 7
        y2 = 6

        txt = Text("Line Conversion")
        txt2 = Text("Incremental Algorithm").set_color(
            ORANGE).next_to(txt, DOWN).scale(1.2)
        self.play(Create(txt), Create(txt2))
        self.wait(4)
        self.remove(txt, txt2)

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True,
                         "font_size": 18},
            tips=False
        )
        plane = NumberPlane(
            x_range=(0, 10, 1),
            y_range=(0, 10, 1),
            x_length=6,
            y_length=6
        )

        pos_1 = axes.coords_to_point(x1, y1)
        pos_2 = axes.coords_to_point(x2, y2)

        p1 = Dot(pos_1, color=GREEN)
        p2 = Dot(pos_2, color=GREEN)
        p1_text = Text('(' + str(x1) + ',' + str(y1) + ')',
                       font_size=18).next_to(p1, DOWN)
        p2_text = Text('(' + str(x2) + ',' + str(y2) + ')',
                       font_size=18).next_to(p2, RIGHT,)

        self.play(Create(plane), Create(axes))
        self.play(Create(p1), Create(p2))
        self.play(Create(p1_text), Create(p2_text))

        self.camera.frame.save_state()

        # txt1 = Text("Step 1: Finding the equation").move_to(
        #     RIGHT*5.3 + UP*2).scale(0.3)
        # self.play(self.camera.frame.animate.set(
        #     width=txt.width).move_to(txt1), run_time=3)
        # self.play(Create(txt1))
        # self.wait(0.5)

        m = (y2-y1)/(x2-x1)  # calculating slop
        c = y1-m*x1
        # txt_m = "{:.2f}".format(m)

        # txt2 = Tex(r"$slope=\frac{y_{2}-y_{1}}{x_{2}-x_{1}} $").move_to(
        #     RIGHT*5.3 + UP*1).scale(0.6)
        # self.play(Create(txt2))
        # self.wait(1)
        # self.remove(txt2)

        # txt2 = Tex("$slope=\\frac{"+str(y2)+"-"+str(y1)+"}{"+str(x2)+"-2}= " + txt_m+"$").move_to(
        #     RIGHT*5.3 + UP*1).scale(0.6)
        # self.play(Create(txt2))
        # self.wait(1)
        # self.remove(txt2)
        # self.play(Restore(self.camera.frame))

        # points = []
        for i in range(x1+1, x2):
            x = i
            y = m*x+c
            y_floor = math.floor(m*x+c)
            y_ceil = math.ceil(m*x+c)

            temp_pixel1 = Rectangle(color=YELLOW, height=0.6, width=0.6, stroke_width=0).move_to(
                axes.coords_to_point(x, y_floor)).set_opacity(1)
            temp_pixel2 = Rectangle(color=YELLOW, height=0.6, width=0.6, stroke_width=0).move_to(
                axes.coords_to_point(x, y_ceil)).set_opacity(1)
            actual_point = Dot(axes.coords_to_point(x, y),
                               color=WHITE, radius=.04)

            self.play(self.camera.frame.animate.set(
                width=4).move_to(actual_point), run_time=1)

            self.play(Create(temp_pixel1), Create(temp_pixel2))
            self.play(Create(actual_point))
            if abs(y-y_floor) < abs(y-y_ceil):
                temp_pixel1.set_color(GREEN)
                temp_pixel2.set_color(RED)
                self.wait(1.5)
                self.remove(temp_pixel2)
                self.wait(0.5)
            else:
                temp_pixel1.set_color(RED)
                temp_pixel2.set_color(GREEN)
                self.wait(1.5)
                self.remove(temp_pixel1)
                self.wait(0.5)

            self.wait(.5)

        self.add(Rectangle(color=GREEN, height=0.6, width=0.6, stroke_width=0).move_to(
            axes.coords_to_point(x1, y1)).set_opacity(1))
        self.add(Rectangle(color=GREEN, height=0.6, width=0.6, stroke_width=0).move_to(
            axes.coords_to_point(x2, y2)).set_opacity(1))
        self.play(Restore(self.camera.frame))

        line = Line(start=pos_1, end=pos_2)
        self.play(Create(line))
        self.wait(1.5)
        self.clear()

        ##

        x1 = 10
        y1 = 5
        x2 = 40
        y2 = 30

        axes = Axes(
            x_range=[0, 50, 1],
            y_range=[0, 50, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True,
                         "font_size": 18},
            tips=False
        )
        plane = NumberPlane(
            x_range=(0, 50, 1),
            y_range=(0, 50, 1),
            x_length=6,
            y_length=6
        )

        pos_1 = axes.coords_to_point(x1, y1)
        pos_2 = axes.coords_to_point(x2, y2)

        p1 = Dot(pos_1, color=GREEN)
        p2 = Dot(pos_2, color=GREEN)
        p1_text = Text('(' + str(x1) + ',' + str(y1) + ')',
                       font_size=18).next_to(p1, DOWN)
        p2_text = Text('(' + str(x2) + ',' + str(y2) + ')',
                       font_size=18).next_to(p2, RIGHT,)

        self.play(Create(plane), Create(axes))
        self.play(Create(p1), Create(p2))
        self.play(Create(p1_text), Create(p2_text))

        self.add(Rectangle(color=GREEN, height=0.12, width=0.12, stroke_width=0).move_to(
            axes.coords_to_point(x1, y1)).set_opacity(1))
        self.add(Rectangle(color=GREEN, height=0.12, width=0.12, stroke_width=0).move_to(
            axes.coords_to_point(x2, y2)).set_opacity(1))

        m = (y2-y1)/(x2-x1)  # calculating slop
        c = y1-m*x1

        for i in range(x1+1, x2):
            x = i
            y = m*x+c
            y_floor = math.floor(m*x+c)
            y_ceil = math.ceil(m*x+c)

            if abs(y-y_floor) < abs(y-y_ceil):
                self.add(Rectangle(color=GREEN, height=0.12, width=0.12, stroke_width=0).move_to(
                    axes.coords_to_point(x, y_floor)).set_opacity(1))
            else:
                self.add(Rectangle(color=GREEN, height=0.12, width=0.12, stroke_width=0).move_to(
                    axes.coords_to_point(x, y_ceil)).set_opacity(1))
            # self.add(Dot(axes.coords_to_point(x, y), color=WHITE, radius=.04))
            self.wait(.1)

        ##

        self.wait(5)

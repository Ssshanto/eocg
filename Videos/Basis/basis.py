# -*- coding: utf-8 -*-
"""Basis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KqyvYvqUkh0DCVaehi5KaGGqtMbqFVz_
"""

!sudo apt update
!sudo apt install libcairo2-dev ffmpeg \
    texlive texlive-latex-extra texlive-fonts-extra \
    texlive-latex-recommended texlive-science \
    tipa libpango1.0-dev
!pip install manim
!pip install IPython --upgrade

from manim import *

# Commented out IPython magic to ensure Python compatibility.
# %%manim -p basis
# 
# class Casper(VGroup):
#     def __init__(self):
#         super().__init__()
#         circle1 = Circle(color=BLUE, fill_opacity=.95)
#         circle2= Circle(color=WHITE, fill_opacity=1)
#         circle3= Circle(color=WHITE, fill_opacity=1)
#         square = Square()
#         triangle = Triangle(color=LIGHT_BROWN, fill_opacity=1)
#         triangle2 = Triangle()
#         
#         circle1.width=2
#         circle1.thickness=3
# 
#         circle2.scale(0.2)
#         circle2.set_stroke( width=1.25)
#         circle2.shift(LEFT* .5)
# 
#         
#         circle3.scale(0.2)
#         circle3.set_stroke( width=1.25)
#         circle3.shift(RIGHT* .5)
# 
#         circle4 = Circle(color=BLACK, fill_opacity=.75)
#         circle4.scale(0.155)
#         circle4.set_stroke( width=1.25)
#         circle4.shift(LEFT* .55)
# 
#         circle5=Circle(color=BLACK, fill_opacity=.75)
#         circle5.scale(0.155)
#         circle5.set_stroke( width=1.25)
#         circle5.shift(RIGHT* .45)
#         
#         square.shift(DOWN *1.75)
#         square.scale(.75)
# 
#         triangle.shift(UP *.65, RIGHT *.42)
#         triangle.scale(.95)
#         triangle.rotate(1.5)
#         triangle.border=2
# 
#         triangle2.shift( DOWN* 2)
#         triangle2.rotate(PI)
#         triangle2.scale(.45)
# 
#         smile = Arc(angle=.75*PI, radius=.2)    
#         smile.rotate(1.15*PI)
#         smile.shift(DOWN * .65)   
# 
#         
#         a = [2, 0, 0]
#         b = [0, 1.75, 0]
#         c = [0, 0, 1.75]
#         
#         ap1 = ArcPolygon(a, b, c, radius=2, color=BLUE, fill_opacity=.75)
#         
#         ap_group = VGroup(ap1).arrange()
#         ap_group.shift(DOWN * 1.75)
#         ap_group.rotate( 1.65* PI * .75)
# 
#         self.add(ap_group, triangle2, circle1, circle2, circle3, circle4, circle5, triangle, smile)
# 
# 
# class basis(Scene):
# 
#       def construct(self):
# 
#         quote=Text("\"If all art aspires to the condition of music,\n all the sciences aspire to the condition of mathematics.\"\n-George Santayana", font_size=25)
#         self.play(Write(quote), run_time=4)
#         self.wait(4)
#         self.remove(quote)
#         self.wait(2)
#         number_plane = NumberPlane(
#             background_line_style={
#                 "stroke_color": TEAL,
#                 "stroke_width": 4,
#                 "stroke_opacity": 0.6
#             }
# 
#         )
#         c=Casper()
#         c.shift(RIGHT*4)
#         c.scale(.6)
#         c.shift(UP*3)
#         self.add(c)
#         self.wait(2)
# 
#         quote=Text("\"But Tasmi! This is Graphics Class!\nWhy are we learning linear algebra again?\"\n-Everyone", font_size=25)
#         quote.to_edge(UP)
#         quote.shift(LEFT)
#         self.play(Write(quote), run_time=4)
#         self.wait(2)
#         quote2=Text("Well...\nLinear Algebra is used for different complex mathematical operations\ntransformations and rendering.", font_size=25, color=BLUE)
#         box = SurroundingRectangle(quote2, color=YELLOW, buff=MED_LARGE_BUFF)
#         g=VGroup(box, quote2)
#         self.play(Create(g),run_time=3)
#         self.wait(5)
#         self.remove(g,c,quote)
#         self.wait(5)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -p basis2
# class basis2(Scene):
# 
#       def construct(self):
#             number_plane = NumberPlane(
#             background_line_style={
#                 "stroke_color": TEAL,
#                 "stroke_width": 4,
#                 "stroke_opacity": 0.6
#             }
#         )
#             self.play(Create(number_plane), run_time=4)
#             self.wait(2)
#             arrow1=Arrow(start=np.array([0,0,0]), end=np.array([1,0,0]), color=RED)
#             self.play(GrowArrow(arrow1))
#             self.wait(2)
#             text3=Text("Any value on the x axis is the multiple of unit vector\nin the x axis Î", font_size=20, color=WHITE, fill_opacity=1)
#             box = BackgroundRectangle(text3, color=BLACK, buff=MED_LARGE_BUFF)
#             gg=VGroup(box, text3)
#             gg.shift(UP*3, RIGHT*3)
#             self.play(Create(gg))
#             self.wait(3)
#             text=Text("1 Î", font_size=25)
#             text.shift(np.array([1,.75,0]))
#             self.add(text)
#             self.wait(2)
#             self.remove(arrow1,text)
#             self.wait(2)
#             arrow1=Arrow(start=np.array([0,0,0]), end=np.array([4,0,0]), color=RED)
#             self.play(GrowArrow(arrow1))
#             text=Text("4xÎ", font_size=25)
#             text.shift(np.array([4,.75,0]))
#             self.add(text)
#             self.wait(2)
#             self.remove(arrow1,text,gg)
# 
# 
# 
#             arrow1=Arrow(start=np.array([0,0,0]), end=np.array([0,1,0]), color=RED)
#             self.play(GrowArrow(arrow1))
#             self.wait(2)
#             text3=Text("Any value on the y axis is the multiple of unit vector\nin the y axis Ĵ ", font_size=20, color=WHITE, fill_opacity=1)
#             box = BackgroundRectangle(text3, color=BLACK, buff=MED_LARGE_BUFF)
#             gg=VGroup(box, text3)
#             gg.shift(DOWN*3, LEFT*3)
#             self.play(Create(gg))
#             self.wait(3)
#             text=Text("1 Ĵ ", font_size=25)
#             text.shift(np.array([.75,1,0]))
#             self.add(text)
#             self.wait(2)
#             self.remove(arrow1,text)
#             self.wait(2)
#             arrow1=Arrow(start=np.array([0,0,0]), end=np.array([0,4,0]), color=RED)
#             self.play(GrowArrow(arrow1))
#             text=Text("4xĴ ", font_size=25)
#             text.shift(np.array([.75,3.5,0]))
#             self.add(text)
#             self.wait(2)
#             self.remove(arrow1,text,gg)
#             self.play(Uncreate(number_plane))
# 
# 
# 
# 
# 
# 
# 
#             self.wait(3)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -p CoordinateSystemExample
# class CoordinateSystemExample(Scene):
#     def construct(self):
#         axes = Axes(
#             # x-axis ranges from -1 to 10, with a default step size of 1
#             x_range=(-1, 10),
#             # y-axis ranges from -2 to 2 with a step size of 0.5
#             y_range=(-2, 2, 0.5),
#      
#             axis_config={
#                 "stroke_color": GREY_A,
#                 "stroke_width": 2,
#             },
#             # Alternatively, you can specify configuration for just one
#             # of them, like this.
#             y_axis_config={
#                 "include_tip": False,
#             }
#         ).add_coordinates()
#       
#         self.add(axes)
#         dot = Dot(color=RED)
#         arrow=Arrow(color=GREEN, start=axes.c2p(0,0), end=axes.c2p(3,2))
#         dot.move_to(axes.c2p(0, 0))
#         self.play(FadeIn(dot, scale=0.5))
#         self.play(dot.animate.move_to(axes.c2p(3, 2)))
#         self.play(GrowArrow(arrow))
#         self.wait(1)
#         self.remove(arrow)
#         self.wait(2)
#         self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
#         arrow1=Arrow(color=GREEN, start=axes.c2p(0,0), end=axes.c2p(5,0.5))
#         self.play(GrowArrow(arrow1))
#         self.wait(2)
#         text4=Text("Once you understand that how the unit axis works\nyou can clearly reach any point on the coordinate system\nWhich is the heart of understanding basis", font_size=20, color=WHITE, fill_opacity=1)
#         box = BackgroundRectangle(text4, color=BLACK, buff=MED_LARGE_BUFF)
#         gg=VGroup(box, text4)
#         gg.shift(DOWN*2, LEFT*3)
#         self.play(Create(gg), run_time=4)
#         self.wait(5)
# 
#         # Similarly, you can call axes.point_to_coords, or axes.p2c
#         # print(axes.p2c(dot.get_center()))
#

# Commented out IPython magic to ensure Python compatibility.
# %%manim -p basisfinal
# 
# class Casper(VGroup):
#     def __init__(self):
#         super().__init__()
#         circle1 = Circle(color=BLUE, fill_opacity=.95)
#         circle2= Circle(color=WHITE, fill_opacity=1)
#         circle3= Circle(color=WHITE, fill_opacity=1)
#         square = Square()
#         triangle = Triangle(color=LIGHT_BROWN, fill_opacity=1)
#         triangle2 = Triangle()
#         
#         circle1.width=2
#         circle1.thickness=3
# 
#         circle2.scale(0.2)
#         circle2.set_stroke( width=1.25)
#         circle2.shift(LEFT* .5)
# 
#         
#         circle3.scale(0.2)
#         circle3.set_stroke( width=1.25)
#         circle3.shift(RIGHT* .5)
# 
#         circle4 = Circle(color=BLACK, fill_opacity=.75)
#         circle4.scale(0.155)
#         circle4.set_stroke( width=1.25)
#         circle4.shift(LEFT* .55)
# 
#         circle5=Circle(color=BLACK, fill_opacity=.75)
#         circle5.scale(0.155)
#         circle5.set_stroke( width=1.25)
#         circle5.shift(RIGHT* .45)
#         
#         square.shift(DOWN *1.75)
#         square.scale(.75)
# 
#         triangle.shift(UP *.65, RIGHT *.42)
#         triangle.scale(.95)
#         triangle.rotate(1.5)
#         triangle.border=2
# 
#         triangle2.shift( DOWN* 2)
#         triangle2.rotate(PI)
#         triangle2.scale(.45)
# 
#         smile = Arc(angle=.75*PI, radius=.2)    
#         smile.rotate(1.15*PI)
#         smile.shift(DOWN * .65)   
# 
#         
#         a = [2, 0, 0]
#         b = [0, 1.75, 0]
#         c = [0, 0, 1.75]
#         
#         ap1 = ArcPolygon(a, b, c, radius=2, color=BLUE, fill_opacity=.75)
#         
#         ap_group = VGroup(ap1).arrange()
#         ap_group.shift(DOWN * 1.75)
#         ap_group.rotate( 1.65* PI * .75)
# 
#         self.add(ap_group, triangle2, circle1, circle2, circle3, circle4, circle5, triangle, smile)
# 
# 
# class basisfinal(Scene):
# 
#       def construct(self):
# 
#         quote=Text("\"If all art aspires to the condition of music,\n all the sciences aspire to the condition of mathematics.\"\n-George Santayana", font_size=25)
#         self.play(Write(quote), run_time=4)
#         self.wait(4)
#         self.remove(quote)
#         self.wait(2)
#         number_plane = NumberPlane(
#             background_line_style={
#                 "stroke_color": TEAL,
#                 "stroke_width": 4,
#                 "stroke_opacity": 0.6
#             }
# 
#         )
#         c=Casper()
#         c.shift(RIGHT*4)
#         c.scale(.6)
#         c.shift(UP*3)
#         self.add(c)
#         self.wait(2)
# 
#         quote=Text("\"But Tasmi! This is Graphics Class!\nWhy are we learning linear algebra again?\"\n-Everyone", font_size=25)
#         quote.to_edge(UP)
#         quote.shift(LEFT)
#         self.play(Write(quote), run_time=4)
#         self.wait(2)
#         quote2=Text("Well...\nLinear Algebra is used for different complex mathematical operations\ntransformations and rendering.", font_size=25, color=BLUE)
#         box = SurroundingRectangle(quote2, color=YELLOW, buff=MED_LARGE_BUFF)
#         g=VGroup(box, quote2)
#         self.play(Create(g),run_time=3)
#         self.wait(5)
#         self.remove(g,c,quote)
#         self.wait(3)
#         
#         number_plane = NumberPlane(
#             background_line_style={
#                 "stroke_color": TEAL,
#                 "stroke_width": 4,
#                 "stroke_opacity": 0.6
#             }
#         )
#         self.play(Create(number_plane), run_time=4)
#         self.wait(2)
#         arrow1=Arrow(start=np.array([0,0,0]), end=np.array([1,0,0]), color=RED)
#         self.play(GrowArrow(arrow1))
#         self.wait(2)
#         text3=Text("Any value on the x axis is the multiple of unit vector\nin the x axis Î", font_size=20, color=WHITE, fill_opacity=1)
#         box = BackgroundRectangle(text3, color=BLACK, buff=MED_LARGE_BUFF)
#         gg=VGroup(box, text3)
#         gg.shift(UP*3, RIGHT*3)
#         self.play(Create(gg))
#         self.wait(3)
#         text=Text("1 Î", font_size=25)
#         text.shift(np.array([1,.75,0]))
#         self.add(text)
#         self.wait(2)
#         self.remove(arrow1,text)
#         self.wait(2)
#         arrow1=Arrow(start=np.array([0,0,0]), end=np.array([4,0,0]), color=RED)
#         self.play(GrowArrow(arrow1))
#         text=Text("4xÎ", font_size=25)
#         text.shift(np.array([4,.75,0]))
#         self.add(text)
#         self.wait(2)
#         self.remove(arrow1,text,gg)
# 
# 
# 
#         arrow1=Arrow(start=np.array([0,0,0]), end=np.array([0,1,0]), color=RED)
#         self.play(GrowArrow(arrow1))
#         self.wait(2)
#         text3=Text("Any value on the y axis is the multiple of unit vector\nin the y axis Ĵ ", font_size=20, color=WHITE, fill_opacity=1)
#         box = BackgroundRectangle(text3, color=BLACK, buff=MED_LARGE_BUFF)
#         gg=VGroup(box, text3)
#         gg.shift(DOWN*3, LEFT*3)
#         self.play(Create(gg))
#         self.wait(3)
#         text=Text("1 Ĵ ", font_size=25)
#         text.shift(np.array([.75,1,0]))
#         self.add(text)
#         self.wait(2)
#         self.remove(arrow1,text)
#         self.wait(2)
#         arrow1=Arrow(start=np.array([0,0,0]), end=np.array([0,4,0]), color=RED)
#         self.play(GrowArrow(arrow1))
#         text=Text("4xĴ ", font_size=25)
#         text.shift(np.array([.75,3.5,0]))
#         self.add(text)
#         self.wait(2)
#         self.remove(arrow1,text,gg)
#         self.play(Uncreate(number_plane))
#         self.wait(3)
# 
#         axes = Axes(
#         # x-axis ranges from -1 to 10, with a default step size of 1
#         x_range=(-1, 10),
#         # y-axis ranges from -2 to 2 with a step size of 0.5
#         y_range=(-2, 2, 0.5),
#   
#         axis_config={
#             "stroke_color": GREY_A,
#             "stroke_width": 2,
#         },
#         # Alternatively, you can specify configuration for just one
#         # of them, like this.
#         y_axis_config={
#             "include_tip": False,
#         }
#         ).add_coordinates()
#   
#         self.add(axes)
#         dot = Dot(color=RED)
#         arrow=Arrow(color=GREEN, start=axes.c2p(0,0), end=axes.c2p(3,2))
#         dot.move_to(axes.c2p(0, 0))
#         self.play(FadeIn(dot, scale=0.5))
#         self.play(dot.animate.move_to(axes.c2p(3, 2)))
#         self.play(GrowArrow(arrow))
#         self.wait(1)
#         self.remove(arrow)
#         self.wait(2)
#         self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
#         arrow1=Arrow(color=GREEN, start=axes.c2p(0,0), end=axes.c2p(5,0.5))
#         self.play(GrowArrow(arrow1))
#         self.wait(2)
#         text4=Text("Once you understand that how the unit axis works\nyou can clearly reach any point on the coordinate system\nWhich is the heart of understanding basis", font_size=20, color=WHITE, fill_opacity=1)
#         box = BackgroundRectangle(text4, color=BLACK, buff=MED_LARGE_BUFF)
#         gg=VGroup(box, text4)
#         gg.shift(DOWN*2, LEFT*3)
#         self.play(Create(gg), run_time=4)
#         self.wait(5)
# 
# 
#


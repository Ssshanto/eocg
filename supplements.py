from manim import *

class Casper(VGroup):
    def __init__(self):
        super().__init__()
        circle1 = Circle(color=BLUE, fill_opacity=.95)
        circle2= Circle(color=WHITE, fill_opacity=1)
        circle3= Circle(color=WHITE, fill_opacity=1)
        square = Square()
        triangle = Triangle(color=LIGHT_BROWN, fill_opacity=1)
        triangle2 = Triangle()
        
        circle1.width=2
        circle1.thickness=3

        circle2.scale(0.2)
        circle2.set_stroke( width=1.25)
        circle2.shift(LEFT* .5)

        
        circle3.scale(0.2)
        circle3.set_stroke( width=1.25)
        circle3.shift(RIGHT* .5)

        circle4 = Circle(color=BLACK, fill_opacity=.75)
        circle4.scale(0.155)
        circle4.set_stroke( width=1.25)
        circle4.shift(LEFT* .55)

        circle5=Circle(color=BLACK, fill_opacity=.75)
        circle5.scale(0.155)
        circle5.set_stroke( width=1.25)
        circle5.shift(RIGHT* .45)
        
        square.shift(DOWN *1.75)
        square.scale(.75)

        triangle.shift(UP *.65, RIGHT *.42)
        triangle.scale(.95)
        triangle.rotate(1.5)
        triangle.border=2

        triangle2.shift( DOWN* 2)
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
        ap_group.rotate( 1.65* PI * .75)

        self.add(ap_group, triangle2, circle1, circle2, circle3, circle4, circle5, triangle, smile)

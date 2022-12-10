from manim import *
class ConductorBandScene(Scene):
    def construct(self):
        square_bottom=Rectangle(width=6,height=2)
        square_top=square_bottom.copy()
        square_bottom.move_to(1.5*DOWN)
        square_top.move_to(1.5*UP)
        points= self.get_points(square_bottom,square_top)
        dots= self.get_dots(points)
        dots.add_updater(self.update_electron)
        self.add(square_bottom,square_top,dots)
        self.wait(13)
    def get_points(self,box_bottom,box_top):
        return np.array([
            [
                np.random.uniform(-box_bottom.width/2,box_bottom.width/2)+box_bottom.get_center()[0],
                np.random.uniform(-box_bottom.height/2,box_bottom.height*2)+box_bottom.get_center()[1],
                0
            ]
            for _ in range(40)
        ])
    def get_dots(self,points):
        return VGroup(*[
            Dot(radius=0.04,color=BLUE_C).move_to(point)
            for point in points
        ])
    def update_electron(self,dots,dt):
        points=np.array(list(map(Mobject.get_center,dots)))
        for dot in dots:
            dot.center=dot.get_center()
            dot.aceleration=np.array([0,-6,0])
            dot.velocity=3*UP
            dot.center+=dot.velocity*dt
            if dot.center[1]>2:
                dot.center[1]=-2
                dot.center[0]=np.random.uniform(-3,3)
            dot.move_to(dot.center)

class MeltallicSemiConductorScene(Scene):
    def construct(self):
        square_bottom=Rectangle(width=6,height=2)
        square_top=square_bottom.copy()
        square_bottom.move_to(2.5*DOWN)
        square_top.move_to(2.5*UP)
    def get_points(self,box_bottom):
        return np.array([
            [
                np.random.uniform(-box_bottom.width/2,box_bottom.width/2)+box_bottom.get_center()[0],
                np.random.uniform(-box_bottom.height/2,box_bottom.height*2)+box_bottom.get_center()[1],
                0
            ]  
            for _ in range(40)
        ])
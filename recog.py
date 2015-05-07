import math

class Polygon:
    def __init__(self, points):
        self.p = points

    def move(self, pos, angle):
        rads = math.pi*angle/180
        for point in self.p:
            x = point[0]
            y = point[1]
            point[0] = x*cos(rads) + y*sin(rads) + pos[0]
            point[1] = -x*sin(rads) + y*cos(rads) + pos[1]

    def get_pos(self):
        return [i[0] for i in self.p]
            
        

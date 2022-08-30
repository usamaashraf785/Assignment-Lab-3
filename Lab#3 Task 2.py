
"""
Task 2: Write a class called Cylinder, which is derived from the Circle and an additional
parameter of height. In a way, we are saying a Cylinder is a Circle with additional height
instance variable. Write methods to modify the height, calculate the surface area (which should
use the superclass area function) and the volume (which should use the superclass area
function).
"""""
# Parent Class
class circle():
    def __init__(self, r):
        self.radius = r
    def area (self):
        return self.radius**2*3.14
# Child Class

class Cylinder (circle):
    def __init__(self,h,r):
        circle.__init__(self,r)
        self.height = h
    def surfArea (self):
        self.sa = (2*circle.area(self)) + (2*3.14*self.radius*self.height)
        return self.sa

    def Volume (self):
        self.vol = circle.area(self)*self.height
        return self.vol

newcylinder = Cylinder(7,8)
print("Surface Area of cylinder is:",newcylinder.surfArea())
print("Volume of cylinder is:",newcylinder.Volume())


"""
Task 2: Write a class called Cylinder, which is derived from the Circle and an additional
parameter of height. In a way, we are saying a Cylinder is a Circle with additional height
instance variable. Write methods to modify the height, calculate the surface area (which should
use the superclass area function) and the volume (which should use the superclass area
function).
"""""
class circle():
    """
    The class will act as a parent class for the class Cylinder
    :return: (float) area of the circle
    """
    def __init__(self, r):
        self.radius = r
    def area (self):
        return self.radius**2*3.14

class Cylinder (circle):
    """
    The class is a child class of Circle class which will
    inherit methods from base class
    """
    def __init__(self,h,r):
        """
        Function is the constructor
        :param h: (float) height of the cylinder
        :param r: (float) radius of the circle
        """
        circle.__init__(self,r)
        self.__height = h
    def height (self):
        """
        Function is to get the height of the cylinder
        :param h: None
        :return: (float) height of the cylinder
        """
        return self.__height
    def set_height (self,h):
        self.__height = h
    def surfArea (self):
        """
        Function will calculate the surface area of the cylinder
        :param h: None
        :return sa: (float) surface area of the cylinder
        """
        self.sa = (2*circle.area(self)) + (2*3.14*self.radius*self.__height)
        return self.sa

    def Volume (self):
        """
        Function will calculate the volume of the cylinder
        :param h: None
        :return vol: (float) volume of the cylinder
        """
        self.vol = circle.area(self)*self.__height
        return self.vol
if __name__ == "__main__":

    newcylinder = Cylinder(7,8)
    print("Surface Area of cylinder is:",newcylinder.surfArea())
    print("Volume of cylinder is:",newcylinder.Volume())

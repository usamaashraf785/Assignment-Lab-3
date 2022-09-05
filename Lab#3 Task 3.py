"""
Task 3 Write another class called Cylinder2, using composition (as shown in the class diagram)
instead of inheritance (task 2). That is, "a cylinder is composed of a base circle and a height". Write
methods to modify the height, calculate the surface area (which should use the Circle class area
function) and the volume (which should use the Circle class area function).
"""""

# Composite Class
class Circle():
    """
    Circle is a composite class which will give the area of circle to other class
    cylinder by composition
    """
    def __init__(self, r):
        """
        Function is the constructor
        :param r: (float) radius of the circle
        """
        self.radius = r
    def area (self):
        """
        Function will calculate the area of cicle
        :param h: None
        :return radius: (float) radius of the circle
        """
        return self.radius**2*3.14
class Cylinder2():
    """
    Cylinder class will get value of area from class circle by composition
    :return:
    """
    def __init__(self,h,r):
        self.height = h
        self.obj1=Circle(r)
    def SurfArea(self):
        # radius = self.obj1.__init__()
        s = 2 * self.obj1.area()
        a = 2 * 3.14 *self.obj1.radius * self.height
        self.sa = s+a
    #   self.sa = (2 * self.obj1.area()) + (2 * 3.14 *self.radius * self.height)  # 2*Area + 2*pi*r*h
        return self.sa
    def Volume(self):
        self.vol = self.obj1.area() * self.height
        return self.vol

newcylinder = Cylinder2(7,8)
print("Surface Area of cylinder is:",newcylinder.SurfArea())
print("Volume of cylinder is:",newcylinder.Volume())

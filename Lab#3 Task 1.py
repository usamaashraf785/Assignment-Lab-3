"""
Task 1: Write a class called Circle, which has a instance variable, radius. Write methods to
calculate the area of the circle and modify the radius
"""""
class circle():
    def __init__(self, r):
        self.radius = r
    def area (self):
        return self.radius**2*3.14

newcircle = circle(8)
print("Area of Circle is:",newcircle.area())

"""
Task 1: Write a class called Circle, which has a instance variable, radius. Write methods to
calculate the area of the circle and modify the radius
"""""
class Circle():
    """
    Class is made for the calculation of area and modifying the radius
    """
    def __init__(self, r):
        """        Function is a constructor and contains the parameter
        :param r:
        :return : None
        """
        self.__radius = r
    def Area (self):
        """
        Function will calculate the Area
        :param : None
        :return: (float)Area of the circle
        """
        return self.__radius**2*3.14
    def set_radius(self, radius):
        """
        The function will modify the Radius
        :param radius: (float) radius of the circle
        :return: (None)
        """
        self.__radius = radius

    def get_radius(self):
        """
        The function will set the value of radius as a setter
        :return: (float) Radius of the circle
        """
        return self.__radius


if __name__ == "__main__":
    newCircle = Circle(8)
    print("Area of Circle is:",newCircle.Area())





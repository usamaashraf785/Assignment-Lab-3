"""
Task 1: Write a class called Circle, which has a instance variable, radius. Write methods to
calculate the area of the circle and modify the radius
""" ""


class Circle:
    """
    The purpose of the class is to
    """

    def __init__(self, r):
        self.__radius = r  # private object attribute

    def area(self):
        """
        What the function does

        :return: (float) the area of the cirlce
        """
        return self.__radius ** 2 * 3.14

    def set_radius(self, radius):
        """
        Purpose of the function

        :param radius: (float) radius of the circle

        :return: (None)
        """
        self.__radius = radius

    def get_radius(self):
        return self.__radius


if __name__ == "__main__":
    new_circle = Circle(8)
    print("Area of Circle is:", newcircle.area())

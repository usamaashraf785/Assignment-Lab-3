"""
Task 1 Write the codes for all the classes as shown in the class diagram. The toString() method gives a string
description of the object and should display in the given format even when print(obj) is called.
"""
List = ["Eagle bhai", "Suzy", "Kitana", "Tony","Jacky"]

class Animal():
    """
    Class will get the name of the Animal
    :param name: (String) name of the Animal
    :return: name (string)
    """

    def __init__(self,name):
        """
        Function is Constructor of the class Animal
        :param name: (String)
        """
        self.name = name

    def __repr__(self):
        """
        Function will return the name
        :return: name (string)
        """
        print("Name of the Animal is:",self.name)


class Mammal(Animal):
    """
    Class is the child class of the Animal Class
    will return the name of the Mammal
    :return:name (string)
    """
    def __init__(self,name):
        """
        function is the Constructor of the class Mammal
        :param name: (string)
        """
        Animal.__init__(self,name)

    def __repr__(self):
        """
        function will return the name of the Mammal
        :return: name (string)
        """
        return print("Name of the Mammal is:",self.name)


class Cat(Mammal):
    """
    Class is the Child class of class Mammal
    will Inherit the name
    :return:
    :param name: (string)
    """
    def __init__(self,name):
        """
        function is the constructor of the class
        :param name: string
        """
        Mammal.__init__(self,name)

    def __Greets(self):
        """
        function will print the greetings of the cat
        :return: None
        """
        print("Meow")

    def __repr__(self):
        """
        function will tostring the description
        :return: None
        """
        print("The ",self.name,"Greets",Cat.__Greets(self))

class Dog(Mammal):
    """
    this Class is also the child class of the Class Mammal
    :return: name (string) name of the first dog
    :return: name2 (string) name of the 2nd dog
    """
    def __init__(self,name,name2):
        """
        Function is constructor of the class
        :param name: (string) name of the first class
        :param name2: (string) name of the 2nd class
        """
        Mammal.__init__(self,name)
        self.name2 = name2

    def __Greets(self,name):
        """
        function will print the greetings of the first dog
        :param name: (string)
        :return: (string)
        """
        print(name,"Greets Woof!")

    def __Greets1(self,name2):
        """
        function will prints the greetings of 2nd dog
        :param name2: (string)
        :return: name2 (string)
        """
        print(name2,"Greets Woooof!!")

    def __repr__(self):
        """
        function will prints the description of the class dog
        :return: None
        """
        print("The ",self.name," greeting ",self.name2)
        Dog.__Greets(self,self.name)
        Dog.__Greets1(self,self.name2)




if __name__ == "__main__":

    newAnimal = Animal(List[0])
    newAnimal.__repr__()
    newMammal = Mammal(List[1])
    newMammal.__repr__()
    newCat = Cat(List[2])
    newCat.__repr__()
    newDog = Dog(List[3],List[4])
    newDog.__repr__()



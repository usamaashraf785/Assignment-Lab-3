from abc import ABC, abstractmethod
List = ["Animal","Kitana", "Tonny", "Jacky", "Sheru", "Bhalo"]

class Animal(ABC):
    """
    class is the abstract and parent class
    will get the name of animal
    :param name:(string)
    :return name: (string)
    """
    def __init__(self,name):
        """
        Function will return the name
        :return: name (string)
        """
        self.name = name

    def __Greets(self):
        """
        function is abstract will pass the values
        :return: None
        """
        pass

class Cat(Animal):
    """
    class will Inherit the properties from class Animal
    :param name: (string)
    :return:
    """

    def __init__(self,name):
        """
        function is the constructor of the class
        :param name: string
        """
        Animal.__init__(self,name)

    def __Greets(self,name):
        """
        function will print the greetings of the cat
        :return: None
        """

        return print(name,"Greets Meow!")

    def __repr__(self):
        """
        function will tostring the description
        :return: None
        """
        print("The "+self.name+" Greets ", Cat.__Greets(self,self.name))


class Dog(Animal):
    """
    this Class is also the child class of the Class Animal
    :return: name (string) name of the first dog
    :return: name2 (string) name of the 2nd dog
    """
    def __init__(self,name,name2):
        """
        Function is constructor of the class
        :param name: (string) name of the first class
        :param name2: (string) name of the 2nd class
        """
        Animal.__init__(self,name)
        self.name2 = name2
        self.__name = List[3]

    def __Greets(self,name):
        """
        function will print the greetings of the first dog
        :param name: (string)
        :return: (string)
        """
        print(name," Greets woof!")

    def __Greets1(self,name2):
        """
        function will prints the greetings of 2nd dog
        :param name2: (string)
        :return: name2 (string)
        """
        print(name2," Greets woooof!!")

    def __repr__(self):
        """
        function will tostring the description of the class dog
        :return: None
        """
        print("The "+ self.name+ " greeting "+ self.name2)
        Dog.__Greets(self,self.name)
        Dog.__Greets1(self,self.name2)

class BigDog(Dog):
    """
    this Class is the child class of the Class Dog
    :return: name (string) name of the first Bigdog
    :return: name2 (string) name of the 2nd Bigdog
    """
    def __init__(self,name,name2):
        """
        Function is constructor of the class
        :param name: (string) name of the first BigDog
        :param name2: (string) name of the 2nd BigDog
        """
        Dog.__init__(self,name,name2)

    def __Greets(self,name):
        """
        function will print the greetings of the first Bigdog
        :param name: (string)
        :return: (string)
        """
        print(self.name,"Greets Wooow!")

    def __Greets1(self,name2):
        """
        function will print the greetings of the 2nd Bigdog
        :param name: (string)
        :return: (string)
        """
        print(self.name2,"Greets Wooooow!!")

    def __repr__(self):
        """
        function will print the description of the class Bigdog
        :return: None
        """
        print("The " + self.name + " Greeting " + self.name2)
        # print("The ", self.name, " Greeting ", Dog.__name)
        BigDog.__Greets(self,self.name)
        BigDog.__Greets1(self,self.name2)


if __name__ == "__main__":
    newAnimal = Animal(List[0])
    newCat = Cat(List[1])
    newCat.__repr__()
    newDog = Dog(List[2],List[3])
    newDog.__repr__()
    newBigDog = BigDog (List[4],List[5])
    newBigDog.__repr__()


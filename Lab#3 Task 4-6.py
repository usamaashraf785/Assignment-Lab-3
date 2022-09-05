"""
Task 4-6: Shown below is a class diagram showing you 3 classes which you need to implement.
As shown, Person class has 2 instance variables, name and address and methods named:
getName, getAddress, setAddress, toString (which gives a string description of the object and
should display the Person in the given format even when print(obj) is called). There is one
constructor which takes in the name and the address. Similarly, write the class called Student and
Staff. [Double means the answer should be a decimal number].
"""""

class Person():
    """
    this class will have two variables name and address
    :return name: (string) name of the person
    :return address: (string) address of the person
    """

    def __init__(self,name,address):
        """
        This Function is a constructor of the class person
        :param name: (string)
        :param address: (string)
        """
        self.name = name
        self.address = address
    def getName(self):
        """
        this function will get the name of the person
        :return name:(string) name of the person
        """
        return self.name
    def setName(self,name):
        self.name = name
    def getAddress(self):
        """
        this function will get the address of the person
        :return adress: (string) address of the person
        """
        return self.address
    def setAddress(self,address):
        self.address = address
    def __repr__(self):
        return self.name + " R/O " + self.address

if __name__ == "__main__":
    newPerson = Person("Usama","11/1AL")
    print("Name is:",newPerson.getName())
    print("Address is:",newPerson.getAddress())
    print("By Tostring method:",newPerson.__repr__())

class Student():
    """
    The class will get the program year and fee of the student
    by getting name and address from the class person by composition
    :return program: (String)
    :return year: (int)
    :return fee:(float)
    """

    def __init__(self,name,address,program,year,fee):
        """
        this function is the constructor of the class
        :param name: (string)
        :param address: (string)
        :param program: (string)
        :param year: (string)
        :param fee: (string)
        :return
        """
        self.program = program
        self.year = year
        self.fee = fee
        self.obj1 = Person(name,address)
    def getProgram(self):
        """
        This function will het the program of the student
        :return: program (string)
        :param: None
        """
        return self.program
    def setProgram(self,program):
        """
        this function will set the program
        :param program: (string)
        :return: None
        """
        self.program = program
    def getYear(self):
        """
        This function will get the year of Enrolment of the student
        :return: year (string)
        :param: None
        """
        return self.year
    def setYear(self,year):
        self.year = year
    def getFee(self):
        """
        This function will get the fee structure of the student
        :return: fee (string)
        :param: None
        """
        return self.fee
    def setFee(self,fee):
        self.fee = fee
    def __repr__(self):
        return print(self.obj1.name+" R/O "+ self.obj1.address+" Doing "+self.program+
                     " with semester fee of "+ self.fee + " In "+self.year)

if __name__ == "__main__":
    newStudent = Student (newPerson.name , newPerson.address,"BS Software Engineering", 2021 , 58760.98)
    print(newStudent.__repr__())

class Staff():
    def __init__(self,name,address,school,pay):
        self.school = school
        self.pay = str(pay)
        self.obj = Person(name,address)
    def getSchool(self):
        return self.school
    def setSchool(self,scl):
        self.school = scl
    def getPay(self):
        return str(self.pay)
    def setPay(self,pay):
        self.pay = pay
    def __repr__(self):
        return print(self.obj.name+" Resident of "+self.obj.address+" From "+self.school+" Earning "+self.pay+" Dollers ")
if __name__ == "__main__":
    newstaf = Staff(newPerson.name,newPerson.address,"GCUF", 10000)
    print(newstaf.__repr__())
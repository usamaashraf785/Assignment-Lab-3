"""
Task 4-6: Shown below is a class diagram showing you 3 classes which you need to implement.
As shown, Person class has 2 instance variables, name and address and methods named:
getName, getAddress, setAddress, toString (which gives a string description of the object and
should display the Person in the given format even when print(obj) is called). There is one
constructor which takes in the name and the address. Similarly, write the class called Student and
Staff. [Double means the answer should be a decimal number].
"""""

class Person():

    def __init__(self,name,address):
        self.name = name
        self.address = address
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def setAddress(self,ads):
        self.address = ads
    def toString(self):
        print(self.name,"R/O",self.address)

newPerson = Person("Usama","11/1AL")
print("Name is:",newPerson.getName())
print("Address is:",newPerson.getAddress())
print("By Tostring method:",newPerson.toString())

class Student():

    def __init__(self,name,address,program,year,fee):
        self.program = program
        self.year = year
        self.fee = fee
        self.obj = Person(name,address)
    def getProgram(self):
        return self.program
    def setProgram(self,pro):
        self.program = pro
    def getYear(self):
        return self.year
    def setYear(self,yr):
        self.year = yr
    def getFee(self):
        return self.fee
    def setFee(self,fi):
        self.fee = fi
    def toString(self):
        print(self.obj.getName(),"R/O",self.obj.getAddress(),"Doing",self.program,
                     "with semester fee of ", self.fee, " In ",self.year)


newstudent = Student(newPerson.name,newPerson.address,"BS Software Engineering", "2021", "60,000")
print(newstudent.toString())

class Staff():
    def __init__(self,name,address,school,pay):
        self.school = school
        self.pay = pay
        self.obj = Person(name,address)
    def getSchool(self):
        return self.school
    def setSchool(self,scl):
        self.school = scl
    def getPay(self):
        return self.pay
    def setPay(self,py):
        self.pay = py
    def toString(self):
        print(self.obj.name,"Resident of",self.obj.address," From ",self.school," Earning ",self.pay," Dollers ")

newstaf = Staff(newPerson.name,newPerson.address,"GCUF", "10,000")
print(newstaf.toString())
class Calender():
    """
    Class will have instance variables days, months and years
    and display the date
    :return:
    :param:
    """
    def __init__(self):
        """
        function will get the days, months and years from user
        and call the setDate method
        :return
        :param
        """
        self.__days = int(input("Enter a day:"))
        self.__months = int(input("Enter a Month:"))
        self.__years = int(input("Enter a Year:"))
        Calender.modDate(self,self.__days,self.__years,self.__months)
        Calender.setDate(self)

    def modDate(self,days,years,months):
        """
        function will modify the days,months and years
        :param days: int
        :param years: int
        :param months: int
        :return: int days,months,years
        """
        self.__days = days
        self.__months = months
        self.__years = years

    def date(self):
        """
        function will display the date in format dd/mm/yyyy
        :return:
        """
        print(self.__days,"/",self.__months,"/",self.__years)


    def setDate(self):
        """
        function will range the days in between 1 and 31
        and will range the months in between 1 and 12
        :return:
        """
        lstM = [i for i in range(1, 12 + 1)]
        lstD = [i for i in range(1, 31 + 1)]
        if self.__days in lstD:
            return self.__days
        elif self.__days not in lstD:
            print("Day has to be an integer between 1 and 31!")

        elif self.__months in lstM:
            return self.__months
        elif self.__months not in lstM:
            print("TypeError in Months:")
        else:
            print("Days and Months should be Integer")

    def LeapYear(self):
        """
        function will check either the year is leap or not
        :return:
        """

        if (self.__years % 400 == 0) and (self.__years % 100 == 0):
            print("{0} is a leap year".format(self.__years))

        elif (self.__years % 4 == 0) and (self.__years % 100 != 0):
            print("{0} is a leap year".format(self.__years))

        else:
            print("{0} is not a leap year".format(self.__years))

Calender().LeapYear()
Calender().date()
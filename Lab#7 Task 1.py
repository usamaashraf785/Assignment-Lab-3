class Calender:
    """
    Class will have instance variables days, months and years
    and display the date
    :return:
    :param:
    """

    def __init__(self, days, months, years):
        """
        function will get the days, months and years from user
        and call the setDate method
        :return
        :param
        """
        self.__days = days
        self.__months = months
        self.__years = years
        Calender.modDate(self, self.__days, self.__years, self.__months)
        Calender.setDate(self)

    def modDate(self, days, years, months):
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
        return str(self.__days) + "/" + str(self.__months) + "/" + str(self.__years)

    def setDate(self):
        """
        function will range the days in between 1 and 31
        and will range the months in between 1 and 12
        :return:
        """
        lstM = [i for i in range(1, 12 + 1)]
        lstD = [i for i in range(1, 31 + 1)]

        if self.__days not in lstD:
            print("Day has to be an integer between 1 and 31!")

        if self.__months not in lstM:
            print("TypeError in Months:")

    def LeapYear(self):
        """
        function will check either the year is leap or not
        :return:
        """

        if (self.__years % 400 == 0) and (self.__years % 100 == 0):
            return "{0} is a leap year".format(self.__years)

        elif (self.__years % 4 == 0) and (self.__years % 100 != 0):
            return "{0} is a leap year".format(self.__years)

        else:
            return "{0} is not a leap year".format(self.__years)


days = int(input("Enter a day:"))
months = int(input("Enter a Month:"))
years = int(input("Enter a Year:"))

Cal = Calender(days, months, years)

print(Cal.LeapYear())
print(Cal.date())

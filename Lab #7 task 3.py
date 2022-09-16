"""
****************************************************************************
                        Class Calendar
****************************************************************************
"""
class Calendar():
    """
    Class will have instance variables days, months and years
    and display the date
    :return:
    :param:
    """
    def __init__(self,days,months,years):
        """
        function will get the days, months and years from user
        and call the setDate method
        :return
        :param
        """
        self.days = days
        self.months = months
        self.years = years
        Calendar.modDate(self,self.days,self.years,self.months)
        Calendar.setDate(self)

    def modDate(self,days,years,months):
        """
        function will modify the days,months and years
        :param days: int
        :param years: int
        :param months: int
        :return: int days,months,years
        """
        self.days = days
        self.months = months
        self.years = years

    def setDate(self):
        """
        function will range the days in between 1 and 31
        and will range the months in between 1 and 12
        :return: print statement
        """
        lstM = [i for i in range(1, 12 + 1)]
        lstD = [i for i in range(1, 31 + 1)]

        if self.days not in lstD:
            print("Day has to be an integer between 1 and 31!")

        if self.months not in lstM:
            print("TypeError in Months:")



"""
********************************************************************************************
                        Class Clock
********************************************************************************************
"""
class Clock():
    """
    Class will have instance variables hours, minutes and seconds
    and display the time
    :return:
    :param:
    """
    def __init__(self,hours,minutes,seconds):
        """
        function will get the input for hours, minutes and seconds
        :return
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        Clock.modClock(self,self.hours,self.minutes,self.seconds)
        Clock.setClock(self)

    def modClock(self,hours,minutes,seconds):
        """
        function will modify the years,minutes and seconds
        :param hours: int
        :param minutes: int
        :param seconds: int
        :return: int hour,minutes,seconds
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def setClock(self):
        """
        function will check the range of the hours in between 0 and 23
        and will range the minutes and seconds in between 0 and 59
        :return: print statement
        """
        lstH = [i for i in range(0, 23 + 1)]
        lstMS = [i for i in range(0, 59 + 1)]

        if self.hours not in lstH:
            print("Hour has to be an integer between 0 and 23!")

        if self.minutes not in lstMS:
            print("Minutes should be of integer type between 0 and 59!")

        if self.seconds not in lstMS:
            print("Seconds should be of integer type between 0 and 59!")



class ClockCalendar (Calendar and Clock):
    """
    class is the child class of the base classes calendar and Clock
    :return
    """

    def __init__(self,days,months,years,hours,minutes,seconds):
        """
        funcion will get the values of days,months,years,hours,minutes and seconds
        :param days: int
        :param months: int
        :param years: int
        :param hours: int
        :param minutes: int
        :param seconds: int
        """
        Calendar.__init__(self,days,months,years)
        Clock.__init__(self,hours,minutes,seconds)

if __name__ == "__main__":
    c = ClockCalendar(4, 23, 2019, 9, 55, 0)
    print(c.days)
    print(c.months)
    print(c.years)
    print(c.hours)
    print(c.minutes)
    print(c.seconds)

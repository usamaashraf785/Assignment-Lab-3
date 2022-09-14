class Clock():
    """
    Class will have instance variables hours, minutes and seconds
    and display the time
    :return:
    :param:
    """
    def __init__(self):
        """
        function will get the input for hours, minutes and seconds
        :return
        """
        self.__hours = int(input("Enter an Hour:"))
        self.__minutes = int(input("Enter Minutes:"))
        self.__seconds = int(input("Enter Seconds:"))
        Clock.modClock(self,self.__hours,self.__minutes,self.__seconds)
        Clock.setClock(self)

    def modClock(self,hours,minutes,seconds):
        """
        function will modify the years,minutes and seconds
        :param hours: int
        :param miinutes: int
        :param seconds: int
        :return: int hour,minutes,seconds
        """
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    def setClock(self):
        """
        function will check the range of the hours in between 0 and 23
        and will range the minutes and seconds in between 0 and 59
        :return:
        """
        lstH = [i for i in range(0, 23 + 1)]
        lstMS = [i for i in range(0, 59 + 1)]
        if self.__hours in lstH:
            return self.__hours
        elif self.__hours not in lstH:
            print("Hour has to be an integer between 0 and 23!")

        elif self.__minutes in lstMS:
            return self.__minutes
        elif self.__minutes not in lstMS:
            print("Minutes should be of integer type between 0 and 59!")
        elif self.__seconds in lstMS:
            return self.__seconds
        else:
            print("Seconds should be of integer type between 0 and 59!")


    def Time(self):
        """
        function will display the time
        :return:
        """
        print(self.__hours,":",self.__minutes,":",self.__seconds)

Clock().Time()
class Clock:
    """
    Class will have instance variables hours, minutes and seconds
    and display the time
    :return:
    :param:
    """
    def __init__(self, hours , minutes , seconds):
        """
        function will get the input for hours, minutes and seconds
        :return
        """
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        Clock.modClock(self,self.__hours,self.__minutes,self.__seconds)
        Clock.setClock(self)

    def modClock(self, hours , minutes , seconds):
        """
        function will modify the years,minutes and seconds
        :param hours: int
        :param minutes: int
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
        :return: print statement
        """
        lstH = [i for i in range(0, 23 + 1)]
        lstMS = [i for i in range(0, 59 + 1)]

        if self.__hours not in lstH:
            print("Hour has to be an integer between 0 and 23!")


        if self.__minutes not in lstMS:
            print("Minutes should be of integer type between 0 and 59!")

        if self.__seconds not in lstMS:
            print("Seconds should be of integer type between 0 and 59!")


    def Time(self):
        """
        function will display the time
        :return: str Description
        """
        return str(self.__hours) +":"+ str(self.__minutes)+ ":" + str(self.__seconds)

hours = int(input("Enter an Hour:"))
minutes = int(input("Enter Minutes:"))
seconds = int(input("Enter Seconds:"))

clk = Clock(hours, minutes, seconds)

print(clk.Time())
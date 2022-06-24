from time import time

class Timer:
    def __init__(self):
        self.__startTimestamp = 0
        self.__endTimestamp = 0

    def startTimer(self):
        self.__startTimestamp = time()

        return self.__startTimestamp

    def endTimer(self):
        self.__endTimestamp = time()

        return self.passedTime()

    def passedTime(self):
        return self.__endTimestamp - self.__startTimestamp
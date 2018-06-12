import logger

class Student:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


studentOne = Student("Peter")
# LOGGER = Logger("oopDemo01")

myName = studentOne.getName()
# LOGGER.logInfo ("Student name: ", myName)
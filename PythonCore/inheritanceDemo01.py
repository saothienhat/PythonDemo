class Person:
    def __init__(self, first, last):
        self.firstn = first
        self.lastn = last

    def getName(self):
        return self.firstn + " " + self.lastn

class Emp(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffno = staffnum

    def getEmpName(self):
        return self.getName() + ", " +  self.staffno

a = Person("Alex", "Karlos")
b = Emp("Alex", "Karlos", "A102")

print(a.getName())
print(b.getEmpName())
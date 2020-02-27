class AppDate:
    second = 0
    minute = 0
    hour = 0
    day = 0
    month = 0
    year = 0

    def __init__(self, day, month, year):
        self.second = 0
        self.minute = 0
        self.hour = 0
        self.day = day
        self.month = month
        self.year = year

    def getDay(self): return self.day

    def getMonth(self): return self.month

    def getYear(self): return self.year

    def setDay(self, day): self.day = day

    def setMonth(self, month): self.month = month

    def setYear(self, year): self.year = year

    def toAppDate(self, day, month, year): return AppDate(day, month, year)

class Chart:

    def __init__(self, title, width=0, heigh=0):
        self.title = title
        self.width = width
        self.heigh = heigh

    def setWidth(self, value): self.width = value

    def getWidth(self): return self.width

    def setHeight(self, value): self.heigh = value

    def getHeight(self): return self.heigh
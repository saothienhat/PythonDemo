class Polygon:

    def __init__(self, noOfSides):
        self.noOfSides = noOfSides
        self.sides = [0 for i in range(noOfSides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.noOfSides)]

    def displaySides(self):
        for i in range(self.noOfSides):
            print("Side", i + 1, "is:", self.sides[i])

    def getType(self):
        return 'Polygon'

    def __str__(self):
        return 'The {} has {} sides'.format(self.getType(), self.noOfSides)
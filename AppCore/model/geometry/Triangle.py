from AppCore.model.geometry.Polygon import Polygon


class Triangle(Polygon):

    def __init__(self):
        super().__init__(3)

    def getType(self):
        return 'Triangle'

    def calArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area

    def displayMultipleInheritanceLevel(self):
        # Display Multiple Inheritance level of the Triangle class
        print(Triangle.mro())

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def toFahrenheit(self):
        return (self.getTemperature() * 1.8) + 32

    def getTemperature(self):
        return self._temperature

    def setTemperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

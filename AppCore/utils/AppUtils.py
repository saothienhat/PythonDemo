
class AppUtils:

    @staticmethod
    def calSum(numberList):
        """ Calculate Sum from a list """
        if len(numberList) == 0: return 0
        return sum(item for item in numberList)

    @staticmethod
    def findMax(numberList):
        """ Find Max value from a list """
        return max(item for item in numberList)

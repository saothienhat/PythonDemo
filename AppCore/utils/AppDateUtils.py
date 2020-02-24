import datetime
from ..model import AppDate


class AppDateUtils:

    @staticmethod
    def getTodayInAppDate():
        now = datetime.datetime.now()
        return AppDate(now.day, now.month, now.year)

    # Get month name from AppDate object
    # @return month name such as 'June'
    @staticmethod
    def getMonthNameByDate(appDate):
        x = datetime.datetime(appDate.year, appDate.month, appDate.day)
        return x.strftime("%B")

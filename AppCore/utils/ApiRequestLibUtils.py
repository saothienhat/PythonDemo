import requests


##
# API Helper using Requests lib
##
class ApiRequestLibUtils:

    @staticmethod
    def doGet(url):
        return requests.get(url).json()

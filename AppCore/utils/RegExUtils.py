import re


class RegExUtils:

    @staticmethod
    def isMatch(pattern, string):
        """
        Check if a pattern matches
        @return True if match. Otherwise False
        """
        return re.match(pattern, string)

    @staticmethod
    def extractNumbersByString(string):
        """
        Extract numbers from a string
        :return: List of numbers if existed. Otherwise, empty list
        """
        pattern = '\d+'
        return re.findall(pattern, string)

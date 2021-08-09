import os

from AppCore.exceptions import BizException
from AppCore.model.geometry.Triangle import Triangle
from AppCore.utils import MatplotlibHelper, AppLogger, ApiRequestLibUtils
from AppCore.datatype import DictionaryPy
import AppCore.utils.AppFileUtils as FileUtils


class AppTester:
    LOGGER = AppLogger('AppTester')
    matplotlibHelper = None

    def __repr__(self):
        return 'For testing features'

    def runTest_Exception(self):
        self.LOGGER.logInfo('Run testcases for Exception...')
        salary = int(input('Please input a number small than 10: '))
        if salary < 10:
            raise BizException('001')

    def runTest_Inheritance(self):
        self.LOGGER.logInfo('Run testcases for Inheritance...')
        triangle = Triangle()
        triangle.inputSides()
        triangle.displaySides()
        print(triangle.calArea())
        print(Triangle.mro())
        print(triangle)

    def run(self):
        self.LOGGER.logInfo('Running testcase.......')

        #### Write code for testing here:

        ####
        self.LOGGER.logInfo('Finish running testcase !')

########################################################

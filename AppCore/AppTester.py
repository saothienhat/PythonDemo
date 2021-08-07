import os

from AppCore.exceptions import BizException
from AppCore.utils import MatplotlibHelper, AppLogger, ApiRequestLibUtils
from AppCore.datatype import DictionaryPy
import AppCore.utils.AppFileUtils as FileUtils


class AppTester:
    LOGGER = AppLogger('AppTester')
    matplotlibHelper = None

    def __repr__(self):
        return 'For testing features'

    def runTestException(self):
        salary = int(input('Please input a number small than 10: '))
        if salary < 10:
            raise BizException('001')

    def run(self):
        self.LOGGER.logInfo('Running testcase.......')

        #### Write code for testing here:

        ####
        self.LOGGER.logInfo('Finish running testcase !')

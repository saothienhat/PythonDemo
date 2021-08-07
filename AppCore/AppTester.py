import os

from AppCore.utils import MatplotlibHelper, AppLogger, ApiRequestLibUtils
from AppCore.datatype import DictionaryPy
import AppCore.utils.AppFileUtils as FileUtils


class AppTester:
    LOGGER = AppLogger('AppTester')
    matplotlibHelper = None

    def __repr__(self):
        return 'For testing features'

    def run(self):
        self.LOGGER.logInfo('Running testcase.......')

        #### Write code for testing here:

        # FileUtils.openFile('AppMain.py')
        os.mkdir('test')

        ####
        self.LOGGER.logInfo('Finish running testcase !')

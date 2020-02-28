import logging
from AppCore.utils import MatplotlibHelper, AppLogger


class AppMain:
    LOGGER = AppLogger('AppMain')
    matplotlibHelper = None

    def __init__(self):
        self.matplotlibHelper = MatplotlibHelper()

    def showSimpleLine(self):
        self.matplotlibHelper.showLineChart('Simple line chart', 'X axis', 'yLabel', 8, 8, ['AA', 'BB', 'CC', 'DD'], [1, 4, 9, 16])

    def showAllMarkersInfo(self):
        self.LOGGER.logInfo('Show all Markers info of Matplotlib')
        self.matplotlibHelper.showAllMarkersInfo()


################################################################
#       RUN APP
################################################################
appMain = AppMain()

"""
Display Line Chart
"""
# appMain.showSimpleLine()

# Show all markers' name and description in Matplotlib library
appMain.showAllMarkersInfo()

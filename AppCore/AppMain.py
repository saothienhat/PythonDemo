from AppCore.utils.MatplotlibHelper import MatplotlibHelper


class AppMain:
    matplotlibHelper = None

    def __init__(self):
        self.matplotlibHelper = MatplotlibHelper()

    def showSimpleLine(self):
        self.matplotlibHelper.showLineChart('Simple line chart', 'X axis', 'yLabel', 8, 8, ['AA', 'BB', 'CC', 'DD'], [1, 4, 9, 16])

    def showAllMarkersInfo(self):
        self.matplotlibHelper.showAllMarkersInfo()


################################################################
#       RUN APP
################################################################
appMain = AppMain()

"""
Display Line Chart
"""
# appMain.showSimpleLine()

appMain.showAllMarkersInfo()

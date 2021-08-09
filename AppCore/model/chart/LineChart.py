from AppCore.model.chart.Chart import Chart


class LineChart(Chart):

    def __init__(self, title, width=0, heigh=0, xLabels=[], xDataList=[], yDataList=[], color='green', marker='o',
                 lineStyle='dashed', linewidth=1, markersize=12):
        super().__init__(title, width, heigh)
        self.__xLabels = xLabels
        self.__xDataList = xDataList
        self.__yDataList = yDataList
        self.__color = color
        self.__lineStyle = lineStyle
        self.__lineWidth = linewidth
        self.__markerSize = markersize

    def setLineColor(self, color): self.__color = color

    def setLineStyle(self, style): self.__lineStyle = style

    def setLineWidth(self, width): self.__lineWidth = width

    def setMarkerSize(self, size): self.__markerSize = size

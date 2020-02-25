import matplotlib.pyplot as plt
import numpy as np


class MatplotlibHelper:

    # Display a Line chart
    # @param list1: a list of number
    # @param list2: a list of number
    @staticmethod
    def showLineChart(title, xLabel, yLabel, width, heigh, list1, list2):
        plt.title(title)
        plt.xlabel(xLabel)
        plt.yLabel(yLabel)
        plt.figure(figsize=(width, heigh))
        plt.plot(list1, list2)
        # plt.plot(list1, list2, "go")
        plt.show()

    # Display a Bar chart
    # @param isBarH: is true will display a bar H
    @staticmethod
    def showBarChart(title, xLabel, yLabel, labels, dataList, color, isBarH):
        plt.title(title)
        plt.xlabel(xLabel)
        plt.yLabel(yLabel)
        if isBarH:
            plt.barh(labels, dataList, color=color)
        else:
            plt.bar(labels, dataList, color=color)
        plt.show()

    # Display a pie chart
    # @param legend: Legend object
    # @param labels: list of label string
    # @param explode: list of Explode object such as [0, 0.1, 0, 0]
    @staticmethod
    def showPieChart(legend, labels, dataList, explode):
        plt.pie(dataList, explode=explode, labels=labels, shadow=True, startAngle=45)
        plt.axis(True)
        plt.legend(legend)
        plt.show()

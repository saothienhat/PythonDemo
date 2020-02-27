import matplotlib.pyplot as plt


class MatplotlibHelper:
    name = 'matplotlib'

    def __init__(self):
        name = 'matplotlib'


    # Display a Line chart
    # @param list1: a list of number
    # @param list2: a list of number
    @staticmethod
    def showLineChart(title, xLabel, yLabel, width, heigh, list1, list2):
        plt.title(title)
        plt.xlabel(xLabel)
        # plt.yLabel(yLabel)
        plt.figure(figsize=(width, heigh))
        plt.plot(list1, list2)
        # plt.plot(list1)
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


# binh = MatplotlibHelper()
# binh.showPieChart("Legend", ['a', 'b', 'c'], [10, 40, 50], [0, 0.1, 0])
# binh.showBarChart("Title", 'xLabel', 'yLabel', ['a', 'b', 'c'], [12, 17, 20], 'green', False)
# binh.showLineChart('Title', 'xLabel', 'yLabel', 10, 40, [1, 3, 5], [8, 6, 9])
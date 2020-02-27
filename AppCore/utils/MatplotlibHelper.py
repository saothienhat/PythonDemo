import matplotlib.pyplot as plt


# References: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html
class MatplotlibHelper:

    # Display a Line chart
    # @param list1: a list of number
    # @param list2: a list of number
    @staticmethod
    def showLineChart(title, xLabel, yLabel, width, heigh, xDataList, yDataList):
        plt.title(title)
        plt.xlabel(xLabel)
        plt.figure(figsize=(width, heigh))
        # plt.plot(xDataList, yDataList)
        # plt.plot(xDataList)
        # plt.plot(xDataList, yDataList, "go")
        plt.plot(xDataList, yDataList, color='green', marker='o', linestyle='dashed', linewidth=1, markersize=12)
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

    # Show all markers' name and description in Matplotlib library
    @staticmethod
    def showAllMarkersInfo():
        markers = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', 'P', '*', 'h', 'H', '+', 'x',
                   'X', 'D', 'd', '|', '_']
        descriptions = ['point', 'pixel', 'circle', 'triangle_down', 'triangle_up', 'triangle_left', 'triangle_right',
                        'tri_down', 'tri_up', 'tri_left', 'tri_right', 'octagon', 'square', 'pentagon', 'plus (filled)',
                        'star', 'hexagon1', 'hexagon2', 'plus', 'x', 'x (filled)', 'diamond', 'thin_diamond', 'vline',
                        'hline']
        x = []
        y = []
        for i in range(5):
            for j in range(5):
                x.append(i)
                y.append(j)
        plt.figure()
        for i, j, m, l in zip(x, y, markers, descriptions):
            plt.scatter(i, j, marker=m)
            plt.text(i - 0.15, j + 0.15, s=m + ' : ' + l)
        plt.axis([-0.1, 4.8, -0.1, 4.5])
        plt.tight_layout()
        plt.axis('off')
        plt.show()

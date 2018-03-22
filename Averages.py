import numpy as np
from matplotlib import pyplot as plt

def synthesize(data):
    """
    :param data: The data read in from the spreadsheet
    :return:
    """

    totalVals = []

    count = 0
    for i in range(30, len(data), 60):
        point = data[i]


        val = getVals(data, i)
        if val != []:
            totalVals.append(val)
            count += 1

    print(type(totalVals[0][0]))
    plotVals(totalVals, count)


def getVals(data, i):
    """

    :param data: A list of data points read from a spreadsheet
    :param i: The set of points we are centered on
    :return: returns a list of average values from +- 30 from i
    """
    actPow = []
    hwTSet = []
    primT = []
    chActive = []
    primTSet = []
    hWActive = []
    hWTOutlet = []
    synthesized = [actPow, hwTSet, primTSet, chActive, primTSet, hWActive, hWTOutlet]

    l = []
    length = len(data)
    for j in range(i - 30, i + 30):

        if j == length:
            return average(synthesized)


        l.append(data[j])

    for item in l:
        actPow.append((item[1]))
        hwTSet.append((item[2]))
        primT.append((item[3]))
        chActive.append((item[4]))
        primTSet.append((item[5]))
        hWActive.append((item[6]))
        hWTOutlet.append((item[7]))

    return average(synthesized)


def average(data):
    """
    :param data: a 2d array of data points in the form [actPow, hwTSet, primT, chActive, primTSet, hwActive, hwTActive]
    :return: returns averaged values of the data points in the form they arrived in
    """
    avs = []  # averages
    for item in data:
        if not len(item) == 0:
            average = sum(item) / len(item)
            avs.append(average)
    return avs


def plotVals(data, count):
    actPow = []
    hwTSet = []
    primT = []
    chActive = []
    primTSet = []
    hWActive = []
    hWTOutlet = []
    print(len(data), type(data[0][0]))

    for item in data:
        # print(item)
        actPow.append(item[0])
        hwTSet.append(float(item[1]))
        primT.append(float(item[2]))
        chActive.append(float(item[3]))
        primTSet.append(float(item[4]))
        hWActive.append(float(item[5]))
        hWTOutlet.append(float(item[6]))

    plot = plt.plot(range(count), actPow)
    plt.setp(plot, color='r')
    plt.show()
    return


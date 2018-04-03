import os
import sys
import Reader as r
import ByTimeFunctions as a
from matplotlib import pyplot as plt
import numpy as np
import pandas


def findDaysInCommon():
    dates = {}
    fiveDays = {}
    rootDir = './RawWBData/'
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in sorted(fileList):
            ending = fname.split('.')[1]
            if (ending == 'csv'):
                date = fname.split('_')[-1]
                newDate = date.split('.')[0]


                if newDate not in dates.keys():
                    dates.update({newDate: [1, dirName + "/" + fname]})
                else:
                    dates[newDate][0] += 1
                    dates[newDate].append(dirName + '/' + fname)

        for item in dates:
            if dates[item][0] >= 5:
                l = []
                for file in dates[item][1::]:

                    day = r.openFile(file)
                    l.append(day)
                fiveDays.update({item: l})



        for item in fiveDays:
            print(item, len(fiveDays[item]))

        for day in fiveDays:
            getDataForFiveDays(day, fiveDays[day])

def getDataForFiveDays(date , data):

    actPowStdDev, primTSetStdDev, chActiveStdDev, primTSetStdDev, hWActiveStdDev, hWTOutletStdDev = a.stdDevByTime(data)
    actPowAvg, primTAvg, chActiveAvg, primTSetAvg, hWActiveAvg, hWTOutletAvg = a.averagesByTime(data)

    # xAxis = range(len(hWTOutletStdDev))
    # plt.plot(xAxis, actPowAvg)
    # plt.plot(xAxis, actPowStdDev)
    #
    #
    # # plt.setp(plot, color='g')
    # plt.title(date)
    # plt.show()

    x = range(len(chActiveStdDev))
    times = []
    for time in pandas.date_range('00:00', None, periods=len(chActiveStdDev), freq='10S'):
        times.append(str(time).split(' ')[-1])
    sampleAndGraph(times, actPowAvg)

    # # print(np.array(x).shape, np.array(actPowStdDev).shape)
    # # print(np.array(x).shape == np.array(actPowStdDev).shape)
    # plt.plot(times, actPowAvg, color='green')
    # plt.plot(times, hWTOutletAvg, color='skyblue')
    # plt.title(date)
    #
    #
    # plt.legend(['actpowavg', 'hwtoutletavg'], loc='upper left')
    # #
    # plt.show()
    return

def sampleAndGraph(data, times):

    plt.plot(times[::50], data[::50])
    plt.show()





if __name__ == '__main__':
    findDaysInCommon()

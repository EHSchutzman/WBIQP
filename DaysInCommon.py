import os
import sys
import Reader as r
import ByTimeFunctions as a
from matplotlib import pyplot as plt
import numpy as np
import pandas

#TODO: Also try to graph all of the data from a day, rather than averaging values, look into just plotting 5 days as lines

def findDaysInCommon():

        dates = makeFilesDictionary()

        fiveDays = {}
        for item in dates:
            if dates[item][0] >= 5:
                l = []
                for file in dates[item][1::]:

                    day = r.openFile(file)
                    l.append(day)
                fiveDays.update({item: l})

        for day in fiveDays:
            getDataForFiveDays(day, fiveDays[day])
        print(len(fiveDays.keys()))
def getDataForFiveDays(date , data):
    actPowStdDev, primTStdDev, chActiveStdDev, primTSetStdDev, hWActiveStdDev, hWTOutletStdDev = a.stdDevByTime(data)
    actPowAvg, primTAvg, chActiveAvg, primTSetAvg, hWActiveAvg, hWTOutletAvg = a.averagesByTime(data)



    # xAxis = range(len(hWTOutletStdDev))
    # plt.plot(xAxis, actPowAvg)
    # plt.plot(xAxis, actPowStdDev)
    #
    #
    # # plt.setp(plot, color='g')
    # plt.title(date)
    # plt.show()
    #
    # x = range(len(chActiveStdDev))
    times = []
    for time in pandas.date_range('00:00', None, periods=len(chActiveStdDev), freq='10S'):
        times.append(str(time).split(' ')[-1])
    sampleAndGraph([actPowAvg, primTAvg], times, ['ActPowAvg', 'PrimTAvg'], date)

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

def sampleAndGraph(data, times, legend, date):


    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    for item in data:
        ax1.plot(times, item)


    plt.legend(legend, loc='upper left')
    plt.title(date)
    plt.xlabel('Time', fontsize=12)



    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax1.get_xticklabels()[::700], visible=True)
    plt.xticks(fontsize=10, rotation=90)
    for tic in ax1.xaxis.get_major_ticks():
        if (ax1.xaxis.get_major_ticks().index(tic) % 700 == 0):
            continue
        else:
            tic.tick1On = tic.tick2On = False
            tic.label1On = tic.label2On = False

    plt.gcf().subplots_adjust(bottom=0.23)

    plt.xlabel("Time of Day", labelpad=10)


    plt.show()


def makeFilesDictionary():
    dates = {}
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
    return dates

if __name__ == '__main__':
    findDaysInCommon()

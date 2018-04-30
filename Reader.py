import csv

import datetime
import numpy as np
import pandas
import xlrd
from matplotlib import pyplot as plt
import ByTimeFunctions as abt
import sys
import os
import chooseafile as caf

#import matplotlib as mat
#from matplotlib import pyplot as pl


def main():
    rootDir = './RawWBData/'
    directories = [] # directories is a 3d array containing all of the days in the collected data
    for dirName, subdirList, fileList in os.walk(rootDir):
        days = []
        for fname in sorted(fileList):
            ending = fname.split('.')[1]
            if (ending == 'csv'):
                dataSheet = openFile(dirName + '/' + fname) # a single day read into a list
                days.append(np.array(dataSheet))
            else:
                pass
        if not len(days) == 0:
            directories.append(np.array(days))


    directories = np.array(directories)

    #This is where our stats things go, directories is a 3d array of [dirs [list of days]]


    for directory in directories:
        actPowAvg, primTAvg, chActiveAvg, primTSetAvg, hWActiveAvg, hWTOutletAvg =  abt.averagesByTime(directory)

        times = []
        for time in pandas.date_range('00:00', None, periods=8300, freq='10S'):
            times.append(str(time).split(' ')[-1])

        fig = plt.figure()

        ax1 = fig.add_subplot(111)

        ax1.plot(times, chActiveAvg)


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
        plt.legend(['Central Heating Active'], loc='lower right')

        plt.title("Central Heating Active Across Time")

        plt.show()
    return


def openFile(filename):
    """
    :param filename: the path of a csv or xls file that needs to be opened and read into a list
    :return: returns the csv or xls data in a list
    """

    time = 0
    actPow = None
    hWTSet = None
    primTSet = None
    primT = None
    chActive = None
    hWTOutlet = None
    hwActive = None
    data = []
    # print(filename)
    if (filename[-4:] == '.csv'):
        with open(filename) as infile:
            csvReader = csv.reader(infile)
            for row in csvReader:
                if (row[0] == 'Time'):

                    actPow = row.index("ActPow")
                    hWTSet = row.index('HwTSet')
                    primTSet = row.index('PrimTSet')
                    primT = row.index('PrimT')
                    chActive = row.index('ChActive')
                    hWTOutlet = row.index("HwTOutlet")
                    hwActive = row.index('HwActive')
                    pass
                else:
                    newRow = [row[time],row[actPow], row[hWTSet], row[primT], row[chActive],row[primTSet] ,row[hwActive], row[hWTOutlet]]

                    data.append(newRow)
                    #print(row)



    else:
        print(filename)
        workbook = xlrd.open_workbook(filename)
        worksheet = workbook.sheet_by_index(0)
        i = 1
        for i in range(worksheet.nrows):
            row = worksheet.row_values(i)
            if(row[0] == 'Time'):
                actPow = row.index("ActPow")
                hWTSet = row.index('HwTSet')
                primTSet = row.index('PrimTSet')
                primT = row.index('PrimT')
                chActive = row.index('ChActive')
                hWTOutlet = row.index("HwTOutlet")
                hwActive = row.index('HwActive')
            else:
                newRow = [row[time], row[actPow], row[hWTSet], row[primT], row[chActive], row[primTSet], row[hwActive],
                          row[hWTOutlet]]

                data.append(newRow)

    return cleanData(data)


def cleanData(data):
    actPow = 0
    hwTSet = 0
    primT = 5
    chActive = 0
    primTSet = 5
    hWActive = 0
    hWTOutlet = 0
    
    for item in data:
        if not item[1] == '':
            actPow = float(item[1])
            item[1] = float(item[1])
        else:
            item[1] = actPow
        if not item[2] == '':
            hwTSet = float(item[2])
            item[2] = float(item[2])
        else:
            item[2] = hwTSet
        if not item[3] == '' and item[3] != '0':
            primT = float(item[3])
            item[3] = float(item[3])
        else:
            item[3] = primT
        if not item[4] == '':
            chActive = float(item[4])
            item[4] = float(item[4])
        else:
            item[4] = chActive
        if not item[5] == '' and item[5] != '0':
            primTSet = float(item[5])
            item[5] = float(item[5])
        else:
            item[5] = primTSet
        if not item[6] == '':
            hWActive = float(item[6])
            item[6] = float(item[6])
        else:
            item[6] = hWActive
        if not item[7] == '':
            hWTOutlet = float(item[7])
            item[7] = float(item[7])
        else:
            item[7] = hWTOutlet

    return data



def makeTimesForGraph(length):
    times = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(24)]

    return times





if __name__ == '__main__':
    main()
    # makeTimesForGraph(8300)

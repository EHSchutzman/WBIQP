import csv
import numpy as np
import xlrd

import Averages as avs
import ActPHwT as PowerOn
import sys
import os

#import matplotlib as mat
#from matplotlib import pyplot as pl


def main():
    rootDir = './RawWBData/'
    directories = [] # directories is a 3d array containing all of the days in the collected data
    for dirName, subdirList, fileList in os.walk(rootDir):
        days = []
        for fname in fileList:
            ending = fname.split('.')[1]
            if (ending == 'csv' or ending == 'xls'):
                l = openFile(dirName + '/' + fname)
                days.append(np.array(l))

            else:
                pass
        if not len(days) == 0:
            directories.append(np.array(days))
    directories = np.array(directories)

    return


def openFile(filename):
    """
    :param filename: the path of a csv or xls file that needs to be opened and read into a list
    :return: returns the csv or xls data in a list
    """
    data = []
    # print(filename)
    if (filename[-4:] == '.csv'):
        with open(filename) as infile:
            csvReader = csv.reader(infile)
            for row in csvReader:
                if (row[0] == 'Time'):
                    pass
                else:
                    data.append(row)
                    #print(row)



    else:
        workbook = xlrd.open_workbook(filename)
        worksheet = workbook.sheet_by_index(0)
        i = 1
        for i in range(worksheet.nrows):
            row = worksheet.row_values(i)
            if(row[0] == 'Time'):
                pass
            else:
                data.append(row)

    return cleanData(data)


def cleanData(data):
    actPow = 0
    hwTSet = 0
    primT = 0
    chActive = 0
    primTSet = 0
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
        if not item[3] == '':
            primT = float(item[3])
            item[3] = float(item[3])
        else:
            item[3] = primT
        if not item[4] == '':
            chActive = float(item[4])
            item[4] = float(item[4])
        else:
            item[4] = chActive
        if not item[5] == '':
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





if __name__ == '__main__':
    main()

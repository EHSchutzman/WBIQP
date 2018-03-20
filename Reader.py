import csv
import Averages as avs
import sys
import os
import xlrd
import numpy as np
import matplotlib as mat
from matplotlib import pyplot as pl


def main():
    rootDir = './RawWBData'
    data = {}
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            ending = fname.split('.')[1]
            if (ending == 'csv' or ending == 'xls'):
                l = openFile(dirName + '/' + fname)
                avs.synthesize(l)
            else:
                pass

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



    else:
        workbook = xlrd.open_workbook(filename)
        worksheet = workbook.sheet_by_index(0)
        i = 1
        for i in range(worksheet.nrows):
            row = worksheet.row_values(i)
            data.append(row)

    return data





if __name__ == '__main__':
    main()

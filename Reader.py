import csv
import sys
import os
import xlrd
import numpy as np
import matplotlib as mat
from matplotlib import pyplot as pl





def main():


    rootDir = './RawWBData'
    for dirName, subdirList, fileList in os.walk(rootDir):
        # print('Found directory: %s' % dirName)
        # print(len(fileList))
        for fname in fileList:
            openFile(dirName + '/' + fname)
            # print('\t%s' % fname)
            continue



    return


def openFile(filename):
    # print(filename)
    if(filename[-4:] == '.csv'):
        pass

        # with open(filename) as infile:
        #     csvReader = csv.reader(infile)
        #     for row in csvReader:
        #         print(row)
    else:
        workbook = xlrd.open_workbook(filename)
        worksheet = workbook.sheet_by_index(0)
        for i in range(worksheet.nrows):
            row = worksheet.row_values(i)




if __name__ == '__main__':
    main()

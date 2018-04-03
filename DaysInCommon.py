import os
import sys
import Reader as r


def findDaysInCommon():
    dates = {}
    fiveDays = {}
    rootDir = './RawWBData/'
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in sorted(fileList):
            ending = fname.split('.')[1]
            if (ending == 'csv' or ending == 'xls'):
                date = fname.split('_')[-1]
                if date not in dates.keys():
                    dates.update({date: [1, dirName + "/" + fname]})
                else:
                    dates[date][0] += 1
                    dates[date].append(dirName + '/' + fname)

        for item in dates:
            if dates[item][0] >= 5:
                l = []
                for file in dates[item][1::]:

                    day = r.openFile(file)
                    l.append(day)


        for item in dates:
            if dates[item][0] >= 5:
                print(len(dates[item]), dates[item])





if __name__ == '__main__':
    findDaysInCommon()

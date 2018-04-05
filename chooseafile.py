from matplotlib import pyplot as plt
import os
import Reader as read

# The following code takes one day of data of user choice and analyzes it.

def chooseafile():
    # If more HMOS are recorded from, add their name below.
    HMOlist = ["25_McIntyre", "2_Himbleton", "37_Woodstock", "50_Bleinheim", "8_Bozward"]
    # If more data is recorded in the future, add the year, month number below.
    yearlist = ["2017", "2018", "2019"]
    monthlist = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",]

    hmocheck = 1

    while hmocheck == 1:
        print("HMO Names: 25_McIntyre, 2_Himbleton, 37_Woodstock, 50_Bleinheim, 8_Bozward")
        print("")
        HMO = input("Type name of the HMO you wish to analyze: ")
        if HMO in HMOlist:
            print("{} is a correct HMO name".format(HMO))
            hmocheck = 0
        else:
            print("The entered HMO name does not exist")
            hmocheck = 1

    yearcheck = 1

    while yearcheck == 1:
        year = input("Type the year you wish to analyze in Ex: 2018 format: ")
        if year in yearlist:
            yearcheck = 0
        else:
            print("The entered year name is formatted wrong or not a valid year")
            yearcheck = 1

    monthcheck = 1

    while monthcheck == 1:
        month = input("Enter the month of the data in number format, EX: 11 = November, 01 = January")
        if month in monthlist:
            monthcheck = 0
        else:
            print("The month entered is not a month number or not entered correctly")
            monthcheck = 1

    daycheck = 1

    while daycheck == 1:
        day = input("Enter the day of the data in number format")
        intday = int(day)
        if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
            if intday in range(1, 31):
                daycheck = 0
            else:
                print("Enter a day in the month chosen")
                daycheck = 1

        if month == "04" or month == "06" or month == "09" or month == "11":
            if intday in range(1, 30):
                daycheck = 0
            else:
                print("Enter a day in the month chosen")
                daycheck = 1

        if month == "04" or month == "06" or month == "09" or month == "11":
            if intday in range(1, 30):
                daycheck = 0
            else:
                print("Enter a day in the month chosen")
                daycheck = 1

        # doubtful that data will be taken in 2020 for this application / project so no need to check for leap year

        if month == "02":
            if intday in range(1, 28):
                daycheck = 0
            else:
                print("Enter a day in the month chosen")
                daycheck = 1

    if HMO == "25_McIntyre":
        stringstart = "720200236_Data_"
    elif HMO == "2_Himbleton":
        stringstart = "720200260_Data_"
    elif HMO == "37_Woodstock":
        stringstart = "720200288_Data_"
    elif HMO == "50_Bleinheim":
        stringstart = "720200295_Data_"
    elif HMO == "8_Bozward":
        stringstart = "720200262_Data_"
    else:
        print("error in code where likely the start of the string part does not have a check for the new HMO added")

    finalstring = "./RawWBData/{}/{}{} {} {}.csv".format(HMO, stringstart, year, month, day)
    print(finalstring)

    return finalstring

def doesitexist(finalstring, filelist):
    print(finalstring, len(filelist))

    if finalstring in filelist:
        print("Attempting to plot desired day")
        result = "y"
    else:
        result = "n"
    return result


def makelist():
    rootDir = './RawWBData/'
    filenamelist = []  # directories is a 3d array containing all of the days in the collected data
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in sorted(fileList):
            print("{}/{}".format(dirName, fname))
            filenamelist.append("{}/{}/{}".format(rootDir, dirName, fname))

    return filenamelist

def onedayplot(day):

    actPow = []
    hwTSet = []
    primT = []
    chActive = []
    primTSet = []
    hWActive = []
    hWTOutlet = []

    changeday = day[:8300]

    if len(day) >= 8300:
        for item in changeday:
            actPow.append((item[1]))
            hwTSet.append((item[2]))
            primT.append((item[3]))
            chActive.append((item[4]))
            primTSet.append((item[5]))
            hWActive.append((item[6]))
            hWTOutlet.append((item[7]))
        plot = plt.plot(range(0, 8300), primTSet)
        plt.setp(plot, color='g')
        plt.title("plot of single day")
        plt.show()
    else:
        print("This day exists, but does not have enough data points to be considered for plotting")

            #put more plots of interest here!

    return


def chooserun():
    allfiles = makelist()

    requestedpath = chooseafile()
    answer = doesitexist(requestedpath, allfiles)
    if answer == "y":
        onedayplot(read.openFile(requestedpath))
    else:
        print("file does not exist!")

    return


if __name__ == '__main__':
    chooserun()
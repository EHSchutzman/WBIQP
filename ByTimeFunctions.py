import numpy as np
from matplotlib import pyplot as plt
import statistics as st


def averagesByTime(direct):
    actPowByTime, actPowtot, primTByTime, primTtot, chActiveByTime, chActivetot, primTSetByTime, primTSettot, hWActiveByTime, hWActivetot, hWTOutletByTime, hWTOutlettot = formatData(
        direct)

    # array for averages of data points
    actPowAvg = []
    hWTSetAvg = []
    primTAvg = []
    chActiveAvg = []
    primTSetAvg = []
    hWActiveAvg = []
    hWTOutletAvg = []

    length = len(actPowByTime[0])
    for i in range(len(actPowByTime)):
        actPowAvg.append(sum(actPowByTime[i]) / length)
        primTAvg.append(sum(primTByTime[i]) / length)
        chActiveAvg.append(sum(chActiveByTime[i]) / length)
        primTSetByTime.append(sum(primTSetByTime[i]) / length)
        hWActiveAvg.append(sum(hWActiveByTime[i]) / length)
        hWTOutletAvg.append(sum(hWTOutletByTime[i]) / length)

    # plot = plt.plot(range(len(hWTOutletAvg)), actPowAvg)
    # plt.setp(plot, color='g')
    # plt.title(label)
    # plt.show()

    return actPowAvg, primTAvg, chActiveAvg, primTSetAvg, hWActiveAvg, hWTOutletAvg


def stdDevByTime(direct):
    actPowByTime, actPowtot, primTByTime, primTtot, chActiveByTime, chActivetot, primTSetByTime, primTSettot, hWActiveByTime, hWActivetot, hWTOutletByTime, hWTOutlettot = formatData(
        direct)

    # array for averages of data points
    actPowStdDev = []
    hWTSetStdDev = []
    primTStdDev = []
    chActiveStdDev = []
    primTSetStdDev = []
    hWActiveStdDev = []
    hWTOutletStdDev = []

    length = len(actPowByTime[0])
    for i in range(len(actPowByTime)):
        actPowStdDev.append(st.stdev(actPowByTime[i]))
        primTStdDev.append(st.stdev(primTByTime[i]))
        chActiveStdDev.append(st.stdev(chActiveByTime[i]))
        primTSetByTime.append(st.stdev(primTSetByTime[i]))
        hWActiveStdDev.append(st.stdev(hWActiveByTime[i]))
        hWTOutletStdDev.append(st.stdev(hWTOutletByTime[i]))

    # plot = plt.plot(range(len(hWTOutletStdDev)), hWTOutletStdDev)
    # plt.setp(plot, color='b')
    # plt.title(label)
    # plt.show()

    return actPowStdDev, primTStdDev, chActiveStdDev, primTSetStdDev, hWActiveStdDev, hWTOutletStdDev


def formatData(direct):
    # all values in arrays

    actPow = []
    hwTSet = []
    primT = []
    chActive = []
    primTSet = []
    hWActive = []
    hWTOutlet = []

    # These arrays are Nx8300 where each row is a full day's worth of points

    actPowtot = []
    hwTSettot = []
    primTtot = []
    chActivetot = []
    primTSettot = []
    hWActivetot = []
    hWTOutlettot = []

    # These arrays will be 8300xN which will be the transpose of the tot matricies

    actPowByTime = []
    hWTSetByTime = []
    primTByTime = []
    chActiveByTime = []
    primTSetByTime = []
    hWActiveByTime = []
    hWTOutletByTime = []

    for day in direct:

        if (len(day) < 8300):

            continue
        else:
            newDay = [list(x) for x in zip(*day)]

            actPow = newDay[1]
            hwTSet = newDay[2]
            primT = newDay[3]
            chActive = newDay[4]
            primTSet = newDay[5]
            hWActive = newDay[6]
            hWTOutlet = newDay[7]

            for i in range(len(actPow)):
                actPow[i] = float(actPow[i])
                hwTSet[i] = float(hwTSet[i])
                primT[i] = float(primT[i])
                chActive[i] = float(chActive[i])
                primTSet[i] = float(primTSet[i])
                hWActive[i] = float(hWActive[i])
                hWTOutlet[i] = float(hWTOutlet[i])

            actPowtot.append(actPow[:8300])
            hwTSettot.append(hwTSet[:8300])
            primTtot.append(primT[:8300])
            chActivetot.append(chActive[:8300])
            primTSettot.append(primTSet[:8300])
            hWActivetot.append(hWActive[:8300])
            hWTOutlettot.append(hWTOutlet[:8300])

            # The tot arrays are now Nx8300 arrays of the columns now we can sum/average the values

            # We are making the By Time arrays by transposing the tot arrays
        actPowByTime = [list(x) for x in zip(*actPowtot)]
        primTByTime = [list(x) for x in zip(*primTtot)]
        chActiveByTime = [list(x) for x in zip(*chActivetot)]
        primTSetByTime = [list(x) for x in zip(*primTtot)]
        hWActiveByTime = [list(x) for x in zip(*hWActivetot)]
        hWTOutletByTime = [list(x) for x in zip(*hWTOutlettot)]


    return actPowByTime, actPowtot, primTByTime, primTtot, chActiveByTime, chActivetot, primTSetByTime, primTSettot, hWActiveByTime, hWActivetot,hWTOutletByTime, hWTOutlettot


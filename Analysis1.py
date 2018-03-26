import numpy as np

def sheetcomplete(direct):

    #all values in arrays

    actPow = []
    hwTSet = []
    primT = []
    chActive = []
    primTSet = []
    hWActive = []
    hWTOutlet = []

    #all values in arrays of arrays for each sheet

    actPowtot = []
    hwTSettot = []
    primTtot = []
    chActivetot = []
    primTSettot = []
    hWActivetot = []
    hWTOutlettot = []

    #sums

    sumactPow = []
    sumhwTSet = []
    sumprimT = []
    sumchActive = []
    sumprimTSet = []
    sumhWActive = []
    sumhWTOutlet = []

    #averages

    aveactPow = []
    avehwTSet = []
    aveprimT = []
    avechActive = []
    aveprimTSet = []
    avehWActive = []
    avehWTOutlet = []



    for day in direct:

        if(len(day) < 8300):

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


    print(len(actPowtot), len(actPowtot[0]))






    data = [aveactPow]

    return data
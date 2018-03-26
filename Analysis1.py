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




    for sheet in direct:
        for item in range(0,8550):
            actPow.append(float(item[1]))
            hwTSet.append(float(item[2]))
            primT.append(float(item[3]))
            chActive.append(float(item[4]))
            primTSet.append(float(item[5]))
            hWActive.append(float(item[6]))
            hWTOutlet.append(float(item[7]))
        actPowtot.append(actPow)
        hwTSettot.append(hwTSet)
        primTtot.append(primT)
        chActivetot.append(chActive)
        primTSettot.append(primTSet)
        hWActivetot.append(hWActive)
        hWTOutlettot.append(hWTOutlet)


    for tot in actPowtot:
            for i in range (0,8550):
                sumactPow[i] = sumactPow[i] + tot[i]

    for i in range (0,8550):
        aveactPow[i] = sumactPow[i]/8550


    #copy this a million times for each variable


    data = [aveactPow]

    return data
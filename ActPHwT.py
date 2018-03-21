def sheetcomplete(l):

    time = []
    actPow = []
    hwTSet = []
    primT = []
    chActive = []
    primTSet = []
    hWActive = []
    hWTOutlet = []

    actPowstore = 0
    hwTSetstore = 0
    primTstore = 0
    chActstore = 0
    primTSstore = 0
    hWActstore = 0
    hWTOutstore = 0

    for item in l:
        if not item[0] == '':
            timestore = item[0]
            time.append(item[0])
        if not item[1] == '':
            actPowstore = float(item[1])
            actPow.append(float(item[1]))
        if not item[2] == '':
            hwTSetstore = float(item[2])
            hwTSet.append(float(item[2]))
        if not item[3] == '':
            primTstore = float(item[3])
            primT.append(float(item[3]))
        if not item[4] == '':
            chActstore = float(item[4])
            chActive.append(float(item[4]))
        if not item[5] == '':
            primTSstore = float(item[5])
            primTSet.append(float(item[5]))
        if not item[6] == '':
            hWActstore = float(item[6])
            hWActive.append(float(item[6]))
        if not item[7] == '':
            hWTOutstore = float(item[7])
            hWTOutlet.append(float(item[7]))

        if item[0] == '':
            timestore = item[0]
        if item[1] == '':
            actPow.append(actPowstore)
        if item[2] == '':
            hwTSet.append(hwTSetstore)
        if item[3] == '':
            primT.append(primTstore)
        if item[4] == '':
            chActive.append(chActstore)
        if item[5] == '':
            primTSet.append(primTSstore)
        if item[6] == '':
            hWActive.append(hWActstore)
        if item[7] == '':
            hWTOutlet.append(hWTOutstore)

        data = [timestore, actPowstore, hwTSetstore, primTstore, chActstore, primTSstore, hWActstore, hWTOutstore]
        print(data)

    return data
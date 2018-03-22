def sheetcomplete(l):

    time = []
    actPow = []
    hwTSet = []
    primT = []
    chActive = []
    primTSet = []
    hWActive = []
    hWTOutlet = []


    for item in l:
        if not item[0] == '':
            time.append(item[0])
        if not item[1] == '':
            actPow.append(float(item[1]))
        if not item[2] == '':
            hwTSet.append(float(item[2]))
        if not item[3] == '':
            primT.append(float(item[3]))
        if not item[4] == '':
            chActive.append(float(item[4]))
        if not item[5] == '':
            primTSet.append(float(item[5]))
        if not item[6] == '':
            hWActive.append(float(item[6]))
        if not item[7] == '':
            hWTOutlet.append(float(item[7]))

    return data
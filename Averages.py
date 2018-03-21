def synthesize(data):
    """
    :param data: The data read in from the spreadsheet
    :return:
    """
    totalVals = []
    count = 0
    for i in range(30, len(data), 60):
        point = data[i]

        count += 1
        totalVals.append(getVals(data, i))


    #STILL WORKING ON THIS BIT
    actPow = []
    hwTSet = []
    primT = []
    chActive = []
    primTSet = []
    hWActive = []
    hWTOutlet = []

    for item in totalVals:
        if item[0] != 100000.0:
            actPow.append(item[0])
        if item[1] != 100000.0:
            hwTSet.append(item[1])
        if item[2] != 100000.0:
            primT.append(item[2])
        if item[3] != 100000.0:
            chActive.append(item[3])
        if item[4] != 100000.0:
            primTSet.append(item[4])
        if item[5] != 100000.0:
            hWActive.append(item[5])
        if item[2] != 100000.0:
            hWTOutlet.append(item[6])

        #print(actPow)
    #WILL EVENTUALLY WORK CORRECTLY


def getVals(data, i):
    """

    :param data: A list of data points read from a spreadsheet
    :param i: The set of points we are centered on
    :return: returns a list of average values from +- 30 from i
    """
    actPow = []
    hwTSet = []
    primT = []
    chActive = []
    primTSet = []
    hWActive = []
    hWTOutlet = []
    synthesized = [actPow, hwTSet, primTSet, chActive, primTSet, hWActive, hWTOutlet]

    l = []

    for j in range(i - 30, i + 30):
        l.append(data[j])

    for item in l:
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

    return average(synthesized)


def average(data):
    """
    :param data: a 2d array of data points in the form [actPow, hwTSet, primT, chActive, primTSet, hwActive, hwTActive]
    :return: returns averaged values of the data points in the form they arrived in
    """
    avs = []  # averages
    for item in data:
        if not len(item) == 0:
            average = sum(item) / len(item)
            avs.append(average)
        else:
            if len(avs) != 0 and avs[-1] != 100000.0:
                avs.append(avs[-1]) #figuring out how to represent no data
            else:
                avs.append(100000.0)
    return avs
import os
import sys
import difflib as df
import Reader as rd
import Graphing as g



def main(args):
    files = []
    houses = []
    datesSelected = []
    variables = {"actPow": "Actual Power", "hwTSet": "Hot Water Temp Setpoint", "primT" : "Primary Temp",
                 "chActive": "Central Heating Active", "primTSet": "Primary Temp Setpoint",
                 "hWActive": "Hot Water Active", "hWTOutlet": "Hot Water Outlet Temp"}
    columns = {"actPow": 1, "hwTSet": 2, "primT": 3,
                 "chActive": 4, "primTSet": 5,
                 "hWActive": 6, "hWTOutlet": 7}
    dates = getFilesAsDict()

    file, vars, house, date = getDateInformation(dates, variables)
    files.append(file)
    houses.append(house)
    datesSelected.append(date)


    while checkForMoreDates():
        newFile, _, house, date = getDateInformation(dates, variables, True)
        houses.append(house)
        datesSelected.append(date)
        files.append(newFile)

    multiplePlots = False
    if len(vars) > 1:
        multiplePlots = checkMultiplePlots()



    #graph the stufffffffffff

    print(len(files[0][0]), vars, houses, datesSelected)
    axis = []
    for item in files:
        axis.append(getAxis(item, vars, columns))


    #axis is a list of length datesSelected by length vars by length of file












    print(len(axis), len(axis[0]))
    plots = axis[0]

    for i in range(len(axis)):
        if not multiplePlots:
            legend = [variables[var] for var in vars]
            g.makeGraph(plots,vars, legend, date)
        else:
            data = [list(x) for x in zip(*axis)]
            print(len(data), len(data[0]), len(data[0][0]))



def checkMultiplePlots():
    val = input("Do you want to plot each variable on a different plot?: (Y/N)")
    if val.lower() == 'y':
        print("Plotting on separate plots")
        return True
    else:

        return False

def getAxis(day, vars, columns):

    indecies = []
    data = []
    for var in vars:
        indecies.append(columns[var])

    for index in indecies:
        data.append([x[index] for x in day])


    return data





def checkForMoreDates():
    val = input("Do you want to add another date?: (Y/N)")
    if val.lower() == 'y':
        print("Adding more dates:")
        return True
    else:

        return False



def getDateInformation(dates, variables, boolean=False):
    file, date, house = chooseADay(dates)

    if not boolean:
        vars = chooseVariables(variables)
        return rd.openFile(file), vars, date, house

    return rd.openFile(file), "1", date, house

def getFilesAsDict():
    dates = {}
    rootDir = './RawWBData/'
    for dirName, subDirList, fileList in os.walk(rootDir):
        for fname in fileList:
            ending = fname.split('.')[1]
            if (ending == 'csv'):
                date = fname.split('_')[-1]
                newDate = date.split('.')[0]

                if newDate not in dates.keys():
                    dates.update({newDate: [1, dirName + "/" + fname]})
                else:
                    dates[newDate][0] += 1
                    dates[newDate].append(dirName + '/' + fname)

    return dates



def chooseADay(dates):
    date = input("Please input a date in YYYY-MM-DD format:")
    stamp = date.split('-')
    stamp = " ".join(stamp)

    print(stamp)
    if stamp in dates.keys():
        print("The date you entered has been found")
        return chooseAHouse(dates, stamp)
    else:
        print("Date {} not found, please try again".format(stamp))
        chooseADay(dates)



def chooseAHouse(dates, date):
    houses = []
    for item in dates[date][1::]:
        fname = item.split("/")
        houses.append(fname[2])


    house = input("Please choose from the available HMOs: " + " | ".join(houses) + ":")

    closest = df.get_close_matches(house, houses)

    if len(closest) != 0:
        indexOfHouses = houses.index(closest[0])

        file = dates[date][indexOfHouses + 1]
        print("Thank you for selecting {}".format(closest[0]))
        return file, date, closest[0]
    else:
        print("Sorry, we could not figure out which house you meant, please try again!")
        chooseAHouse(dates, date)




def chooseVariables(variables):
    print("Please select the variables you would like to graph.  You may select "
          "multiple variables separating by comma (,)")
    vars = input("The available variables are: " + " | ".join(sorted(variables)) + ":")
    vars = vars.split(",")
    names = list(sorted(variables))
    broken = 0
    variablesToGraph = []
    for var in vars:
        match = df.get_close_matches(var.strip(), names)
        if len(match) == 0:
            print("We were unable to match " + var + "to an actual variable name, please re enter "
                                                     "selected variables again")
            print("\n\n\n")

            broken = 1
            break
        variablesToGraph.append(match[0])
    if broken == 1:
        variablesToGraph = chooseVariables(variables)

    return variablesToGraph






if __name__ == '__main__':
    main(sys.argv)

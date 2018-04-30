import Reader as rd
import chooseafile as ch
import DaysInCommon as dc


def main():
    """This is the main function for the program, input the selected method you want to run"""
    programchoose = input(
        "Type 1 for single day, variable, hmo analysis, 2 for average across HMO analysis and 3 for average across timeslot analysis")
    if (programchoose == 1):
        ch.chooseafile()
    elif (programchoose == 2):
        dc.findDaysInCommon()
    elif (programchoose == 3):
        rd.main()
    else:

        return 0


    return


if __name__ == '__main__':
    main()
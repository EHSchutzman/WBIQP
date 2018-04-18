import pandas
from matplotlib import pyplot as plt
from matplotlib import axes as ax

def makeGraph(yAxis, yLabel, legend, title):
    times = []
    for time in pandas.date_range('00:00', None, periods=8300, freq='10S'):
        times.append(str(time).split(' ')[-1])




    fig = plt.figure()

    ax1 = fig.add_subplot(111)
    for y in yAxis:
        ax1.plot(times, y)

    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax1.get_xticklabels()[::700], visible=True)
    plt.xticks(fontsize=10, rotation=90)
    for tic in ax1.xaxis.get_major_ticks():
        if(ax1.xaxis.get_major_ticks().index(tic) % 700 == 0):
            continue
        else:
            tic.tick1On = tic.tick2On = False
            tic.label1On = tic.label2On = False

    plt.gcf().subplots_adjust(bottom=0.23)

    plt.xlabel("Time of Day", labelpad=10)
    plt.ylabel(yLabel, labelpad=10)

    plt.title(title)

    plt.show()
    return


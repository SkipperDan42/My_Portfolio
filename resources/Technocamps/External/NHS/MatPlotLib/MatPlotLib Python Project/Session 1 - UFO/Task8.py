import math
import matplotlib.pyplot as plot
from operator import itemgetter


def task(allUFOData):
    plot.figure()

    timeDuration = []
    hourStr = "00"
    timeStr = hourStr + ":00"

    allUFOData.sort(key=itemgetter(1))

    for entry in allUFOData:
        if entry[1][:2] == hourStr:
            timeDuration.append([timeStr, float(entry[5].replace("\n", ""))])
        else:
            hourStr = entry[1][:2]
            timeStr = hourStr + ":00"
            timeDuration.append([timeStr, float(entry[5].replace("\n", ""))])


    ## PLOTTING THIS RESULTS IN A VERY UNHELPFUL GRAPH - ##
    ## THIS IS DUE TO SOME MASSIVE DURATIONS RECORDED ##

    #fig5 = plot.scatter([time[0] for time in timeDuration],
                        #[duration[1] for duration in timeDuration])


    ## PLOTTING THE GRAPH LOGARITHMICALLY RESULTS IN NO CLEAR LINK BETWEEN DURATION AND TIME ##

    with plot.style.context('tableau-colorblind10'):
        fig5 = plot.scatter([time[0] for time in timeDuration],
                        [math.log10(duration[1]) for duration in timeDuration])
        plot.xticks(rotation=90)
        plot.title("Duration of UFO Sightings for the Time of Day")
        plot.xlabel("Time of Day")
        plot.ylabel("Duration (log10[seconds])")

    #print(plot.style.available)

    return fig5
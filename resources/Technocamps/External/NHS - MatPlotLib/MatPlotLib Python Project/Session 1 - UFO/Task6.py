import matplotlib.pyplot as plot
from operator import itemgetter

def task(allUFOData):
    plot.figure()

    timeCount = []
    hourStr = "00"
    count = 0

## COULD SORT THROUGH HOURS USING FOR LOOPS - BUT VERY SLOW ##
    ## 24 * 4 * 87,000 = VERY BIG NUMBER OF ITERATIONS ##

    #for hour in range(0,24):
        #if hour < 10:
        #    hourStr = "0" + str(hour)
        #else:
        #    hourStr = str(hour)

        #for minute in range(0,4):
        #    if minute == 0:
        #        timeStr = hourStr + ":0" + str(minute)
        #    else:
        #        timeStr = hourStr + ":" + str(minute * 15)

        #    count = 0
        #    for entry in allUFOData:
        #        if entry[1] == timeStr:
        #            count += 1
        #            timeCount.append([timeStr, count])


## INSTEAD USE BUILT IN SORT FUNCTION TO SORT BY TIME BEFORE LOOPING ##

    allUFOData.sort(key=itemgetter(1))

    for entry in allUFOData:
        if entry[1][:2] == hourStr:
            count += 1
        else:
            timeStr = hourStr + ":00"
            timeCount.append([timeStr, count])
            hourStr = entry[1][:2]
            count = 1



    fig3 = plot.bar([str[0] for str in timeCount],[count[1] for count in timeCount])

    plot.xticks(rotation=90)
    plot.xlabel("Time")
    plot.ylabel("Number of Sightings")
    plot.title("Worldwide Reported Sightings of UFOs by Time")

    return fig3
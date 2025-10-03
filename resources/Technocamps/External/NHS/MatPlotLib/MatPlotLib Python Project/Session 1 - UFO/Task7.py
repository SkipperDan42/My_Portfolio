import matplotlib.pyplot as plot

def task(allUFOData):
    countryCounts = []

    for entry in allUFOData:
        if entry[3] != "":
            if entry[3] not in [country[0] for country in countryCounts]:
                countryCounts.append([entry[3], 1])
            else:
                for country in countryCounts:
                    if country[0] == entry[3]:
                        country[1] += 1

    plot.figure()
    plot.title("Number of UFO Sightings by Country")

    explode = (0.2, 0.2, 0.2, 0.2, 0.2)
    fig4 = plot.pie([counts[1] for counts in countryCounts],
                    explode=explode,
                    labels=[country[0] for country in countryCounts],
                    autopct='%1.1f%%',
                    colors=['crimson', 'orange', 'yellowgreen'])

    return fig4

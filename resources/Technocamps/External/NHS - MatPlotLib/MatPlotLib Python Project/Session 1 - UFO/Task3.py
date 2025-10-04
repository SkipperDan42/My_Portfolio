import matplotlib.pyplot as plot

#Task 2 is to understand how to plot the data that has been read

def task(dietCounts):
    #Create a new figure (window) for the graph
    plot.figure()

    #Plot a bar chart from the list of tuples received
    fig1 = plot.bar([x[0] for x in dietCounts], [y[1] for y in dietCounts])


    #return fig1    <- Each of the following adjustments can be done after the first plot


    ## Once plotted we can begin to fix the plot! ##

    # First of all the x-axis labels overlap and would be better if they were rotated
    plot.xticks(rotation=90)

    # Now that they are rotated the plot must be resized so that they fit.
    plot.subplots_adjust(bottom=0.25)

    # Axes labels can be added to clarify the data
    # (this will require adjusting the bottom of the plot again)
    plot.xlabel("Food Options")
    plot.ylabel("Number of Visits")

    # Finally a title can be added to the plot
    plot.title("A Chart Documenting Dan's Terrible Diet during March 2024")

    return fig1
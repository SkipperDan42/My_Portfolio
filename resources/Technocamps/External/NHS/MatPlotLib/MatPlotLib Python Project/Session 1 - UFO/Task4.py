import matplotlib.pyplot as plot


#Task 4 gives the learners a chance to continue restructuring and plotting data
# - This can be used as an extension task if the learners are quickly progressing
# - Cut out if time is short

def task(dietCounts):
    dietCategories = [["Fast Food", 0], ["Sit Down Meal", 0], ["Home Made", 0]]

    for item in dietCounts:
        if ((item[0] == "Greggs") or (item[0] == "McDonalds") or (item[0] == "Burger King")
                or (item[0] == "Tortilla") or (item[0] == "Chippy") or (item[0] == "Coffee Shop")
                or (item[0] == "Tim Hortons") or (item[0] == "Dominos")):
            dietCategories[0][1] += item[1]

        elif ((item[0] == "Pizza Hut") or (item[0] == "Restaurant")
              or (item[0] == "Pub Grub") or (item[0] == "Canteen")):
            dietCategories[1][1] += item[1]

        elif (item[0] == "Home Cooking") or (item[0] == "Oven Food") or (item[0] == "Packed Lunch"):
            dietCategories[2][1] += item[1]


    #print(dietCategories)

    #Create a new figure (window) for the graph
    plot.figure()

    #Plot a pie chart from the list of tuples
    #fig2 = plot.pie([counts[1] for counts in dietCategories],
    #                labels = [labels[0] for labels in dietCategories])

    # Add a title to the chart
    plot.title("A Pie Chart Documenting the Categories of Dan's Diet during March 2024")

    # Plot a pie chart from with percentages
    #fig2 = plot.pie([counts[1] for counts in dietCategories],
    #                labels=[labels[0] for labels in dietCategories],
    #                autopct='%1.1f%%')

    # And colours
    #fig2 = plot.pie([counts[1] for counts in dietCategories],
    #                labels=[labels[0] for labels in dietCategories],
    #                autopct='%1.1f%%',
    #                colors=['crimson', 'orange', 'yellowgreen'])

    print(dietCategories)

    # Exploded!
    explode = (0, 0, 0.5)
    fig2 = plot.pie([counts[1] for counts in dietCategories],
                    explode=explode, shadow=True,
                    labels=[labels[0] for labels in dietCategories],
                    autopct='%1.1f%%',
                    colors=['crimson', 'orange', 'yellowgreen'])

    return fig2
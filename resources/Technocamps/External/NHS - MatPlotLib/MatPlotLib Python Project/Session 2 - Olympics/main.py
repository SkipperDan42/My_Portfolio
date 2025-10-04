import matplotlib.pyplot as plt
import Task1, Task2, Task3a, Task3b, Task4, Task5a, Task5b, Task6b, Task6a

#NOTE: These tasks do not need to be individual functions
#      for the session.
#      Additionally these are only a guide of increasing difficulty,
#      it is better for the participants to play with this data
#      as opposed to strictly following these tasks.

#Task1 - Load a pandas DateFrame
athleteData = Task1.task()

print(athleteData[(athleteData["Event"] == "Alpine Skiing Men's Downhill")
      & ((athleteData["Medal"] == "Gold")
      | (athleteData["Medal"] == "Silver")
      | (athleteData["Medal"] == "Bronze"))])

#Task2 - Useful pandas operations
Task2.task(athleteData)

#Task3 - Easy plotting with pandas (and then with labels)
fig1, fig2, fig3, fig4, fig5 = Task3a.task(athleteData)
#fig1, fig2, fig3, fig4, fig5 = Task3b.task(athleteData)

#Task4 - Plot a particular set within the DataFrame
fig6 = Task4.task(athleteData, "USA")

#Task5 - Get more specific with data selection
fig7 = Task5a.task(athleteData, "USA", [1980, 1984, 1988, 1992, 1996])
fig8 = Task5b.task(athleteData, 2012, ["USA","GBR","CHN","RUS"])

#Task7 - Plot all data using this grouping (try/except needed)
fig9 = Task6a.task(athleteData, "GBR")
fig10 = Task6b.task(athleteData, 2012)

plt.show()


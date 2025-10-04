import matplotlib.pyplot as plt

import Task1, Task2, Task3, Task4, Task5, Task6, Task7, Task8

#Task1
yearlyConcentration = Task1.task()

#Task2
fig1 = Task2.task(yearlyConcentration)

#Task3
dates, concentration, fig3 = Task3.task()

#Task4
fig4 = Task4.task(dates, concentration)

#Task5
allSeaLevels, allMeasures = Task5.task()

#Task6
seaLevelsByMeasure = Task6.task(allSeaLevels, allMeasures)

#Task7
Task7.task(allMeasures, seaLevelsByMeasure)

#Task8
#Task8.task(allMeasures, seaLevelsByMeasure, 'Tropics', 'Yellow Sea')

plt.show()
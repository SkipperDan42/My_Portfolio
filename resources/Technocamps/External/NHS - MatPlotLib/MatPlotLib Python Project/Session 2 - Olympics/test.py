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

print(athleteData[(athleteData["Event"] == "Archery Women's Individual")
      & (athleteData["Year"] == 2012)
      & ((athleteData["Medal"] == "Gold")
      | (athleteData["Medal"] == "Silver")
      | (athleteData["Medal"] == "Bronze"))])
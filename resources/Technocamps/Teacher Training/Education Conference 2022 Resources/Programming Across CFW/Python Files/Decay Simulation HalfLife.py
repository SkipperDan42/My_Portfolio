from random import randint

# Initial Number of nuclei
initialNuclei = int(input('What is the starting number of nuclei?'))
currentNuclei = initialNuclei

# The probability that a given nucleus will decay
probability = float(input("\nEnter a percentage value for the chance of a nucleus decaying each second \ni.e. 50: "))

seconds = 0
halflife = 0
halflifeFound = False

while currentNuclei > 0:

    # Print the number of nuclei remaining and increase the time by 1.
    print(currentNuclei)
    seconds += 1
    
    # Consider each nucleus in turn and decide whether it decays or not.
    for nuclei in range(currentNuclei):
        rand = randint(0,100)
        if rand < probability:
            currentNuclei -= 1

        if currentNuclei < round(initialNuclei / 2) and halflifeFound == False:
            halflifeFound = True
            halflife = seconds
    
    
print("The half life for this sample is between %d and %d seconds." %(halflife - 1, halflife)) 


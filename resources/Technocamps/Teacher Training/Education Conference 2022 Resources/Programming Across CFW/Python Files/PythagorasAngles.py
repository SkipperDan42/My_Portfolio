from math import sqrt, asin, acos, atan

print('Pythagorean theorem calculator! Calculate your triangle sides and angles')
print('Assume the sides are a, o and h, where h is the hypotenuse (remember h is always the biggest!)')

formula = input('Which side (a, o, h) do you wish to calculate? ')

if formula == 'a':
        sideO = int(input('Input the length of side o: '))
        sideH = int(input('Input the length of side h: '))
    
        sideA = sqrt((sideH * sideH) - (sideO * sideO))

        theta = asin(sideO / sideH)
    
        print('\nThe length of side a is : ' + str(sideA))
        print('\nThe angle given by sin in radians is: ' + str(theta))
        

elif formula == 'o':
        sideA = int(input('Input the length of side a: '))
        sideH = int(input('Input the length of side h: '))

        sideO = sqrt((sideH * sideH) - (sideA * sideA))

        theta = acos(sideA / sideH)
    
        print('\nThe length of side o is : ' + str(sideO))
        print('\nThe angle given by cos in radians is : ' + str(theta))
        

elif formula == 'h':
        sideA = int(input('Input the length of side a: '))
        sideO = int(input('Input the length of side o: '))

        sideH = sqrt((sideA * sideA) + (sideO * sideO))

        theta = atan(sideO / sideA)
	
        print('\nThe length of side h is : ' + str(sideH))
        print('\nThe angle given by tan in radians is : ' + str(theta))
        
else:
        print('Please select a side between a, o, h')

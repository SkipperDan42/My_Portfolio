
#Shape Area Calculator

PI = 3.1415

area = 0

shapeSelection = input("Enter the shape you would like to calculate: ")

#calculates area of a circle or rectangle
#based on shapeSelection by user
if shapeSelection == "circle":

    radius = float(input("What is the radius (cm)? "))

    #circle area calculation
    area = PI * radius ** 2

elif shapeSelection == "rectangle":

    height = float(input("What is the height (cm)? "))
    width = float(input("What is the width (cm)? "))

    #rectangle area calculation
    area = height * width

#displays error message for invalid shapes
else:
    print("Cannot calculate area of a " + shapeSelection)
    print("Area will be given as 0")

#prints the calculated area
print("The area of your", shapeSelection, "is", area, "cm2")

    




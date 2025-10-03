from CircleCalculator import circleArea
from RectangleCalculator import rectangleArea
#Shape Area Calculator
def main():
    area = 0

    shapeSelection = input("Enter the shape you would like to calculate: ")

    if shapeSelection == "circle":

        area = circleArea()

    elif shapeSelection == "rectangle":

        area = rectangleArea()

    #displays error message for invalid shapes
    else:
        print("Cannot calculate area of a " + shapeSelection)
        print("Area will be given as 0")

    #prints the calculated area
    print("The area of your", shapeSelection, "is", area, "cm2")

main()

    




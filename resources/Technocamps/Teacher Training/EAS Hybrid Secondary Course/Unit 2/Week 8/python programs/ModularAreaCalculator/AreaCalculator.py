def areaCalculator(shape):
    #calculates area of a circle or rectangle
    #based on shapeSelection by user
    if shape == "circle":

        radius = float(input("What is the radius (cm)? "))

        #circle area calculation
        return PI * radius ** 2

    elif shape == "rectangle":

        height = float(input("What is the height (cm)? "))
        width = float(input("What is the width (cm)? "))

        #rectangle area calculation
        return height * width

    #displays error message for invalid shapes
    else:
        print("Cannot calculate area of a " + shape)
        print("Area will be given as 0")
        return 0

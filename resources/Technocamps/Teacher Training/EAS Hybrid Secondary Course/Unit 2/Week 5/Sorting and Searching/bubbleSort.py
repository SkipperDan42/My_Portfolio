#Python Bubble Sort Function
 
def bubbleSort(array):
    
    #This optimizes the code, so if the array is already sorted,
    #it doesn't need to go through the entire process
    swapped = False
    
    # Traverse through all array elements
    n = len(array)
    for i in range(n-1):
        #range(n) also works but the outer loop will repeat one time more than needed.
        #Last i element is already in place

        for j in range(0, n-i-1):
            #Traverse the array from 0 to n-i-1

            #Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
         
        if not swapped:
            #If no swap is made for first element we can just exit the main loop.
            return
 
 
#Define array to sort
array = [64, 34, 25, 12, 22, 11, 90]

#Run sort
bubbleSort(array)

#Print sorted array
print("The sorted array is:")
for i in range(len(array)):
    print("% d" % array[i], end=" ")

#Python Insertion Sort Function

def insertionSort(array):
    
    for i in range(1, len(array)):
        
        #Run binary search for values in array (all but first)
        value = array[i]
        j = binarySearch(array, value, 0, i-1)

        #Rearrange array from results of search
        array = array[:j] + [value] + array[j:i] + array[i+1:]

        print("i:", i)
        print("j:", j)
        print("value:", value)
        print("array:", array)
        print()

    print("Sorted array:")
    return array


def binarySearch(array, value, start, end):
    #Should we insert before or after the left boundary?
    #If [0] was the last step, we need to decide where to insert [-1]
    if start == end:
        if array[start] > value:
            return start
        else:
            return start+1
 
    #This occurs if we are moving beyond left boundary
    #i.e. the left boundary is the least position to
    #find a number greater than val
    if start > end:
        return start
 
    mid = (start+end) // 2
    
    if array[mid] < value:
        return binarySearch(array, value, mid+1, end)
    
    elif array[mid] > value:
        return binarySearch(array, value, start, mid-1)
    
    else:
        return mid

startingArray = [23, 0, 17, 12, 4, 5]
print("Starting Array:", startingArray)
print(insertionSort(startingArray))
















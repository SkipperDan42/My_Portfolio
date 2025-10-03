def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key

#mergeSort
def mergeSort(array):

    #ends recursion if list is 1 element or 0 elements
    if len(array) <=1:
        return array
    
    #divide array in half
    midpoint = len(array) // 2
    left_half = array[:midpoint]
    right_half = array[midpoint:]

    #recursive sort both halves
    sorted_left = mergeSort(left_half)
    sorted_right = mergeSort(right_half)

    #merge sorted halves
    return merge(sorted_left, sorted_right)

#merge function for the merge sort
def merge(left, right):
    sorted_array= []
    i = 0
    j = 0

    while i< len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j +=1

    while i < len(left):
                  sorted_array.append(left[i])
                  i += 1

    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array
    

#Python Bubble Sort Function
def bubbleSort(array):

        swapped = True

        # ends early if there have been no swaps
        while swapped:
            swapped = False
            
        # Traverse through all array elements
        #length of array would try to compare outside list at the end (array[i+1])
            for i in range(len(array)-1):
            
                #Swap if the element found is greater than the next element
                if array[i] > array[i+1]:
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp

                    swapped = True #say that a swap has occured

        return array

#function to implement a linear search
def linearSearch(array, value):

    for i in range(len(array)):
        if array[i] == value:
            return i

    return "ERROR: NOT FOUND"
    
 
def main():
    unorderedList = [64, 34, 25, 12, 22, 11, 90]
    sortedList = bubbleSort(unorderedList)

    itemToFind = 34
    
    result = linearSearch(sortedList, itemToFind)

    print("Value at index:", result)

main()












#Python Binary Search Function

def binarySearch(array, value, start, end):
    # we need to distinguish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if array[start] > value:
            return start
        else:
            return start+1
 
    # this occurs if we are moving beyond left\'s boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if start > end:
       return start
 
    mid = (start+end) // 2
    
    if array[mid] < value:
        return binary_search(array, value, mid+1, end)
    elif array[mid] > value:
        return binary_search(array, value, start, mid-1)
    else:
        return mid

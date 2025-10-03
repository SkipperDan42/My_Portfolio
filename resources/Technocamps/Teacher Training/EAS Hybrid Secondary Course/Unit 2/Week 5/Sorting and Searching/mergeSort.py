def merge_sort(arr):
    """
    Recursively divides the array into halves, sorts each half, 
    and merges them back together.
    
    :param arr: List of elements to be sorted
    :return: A sorted list
    """
    if len(arr) <= 1:
        # Base case: an array with 0 or 1 elements is already sorted
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]  # Left half of the array
    right_half = arr[mid:]  # Right half of the array

    # Step 2: Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Step 3: Merge the two sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Merges two sorted arrays into one sorted array.
    
    :param left: Sorted left half
    :param right: Sorted right half
    :return: A merged sorted array
    """
    sorted_array = []  # To store the merged result
    i = j = 0  # Pointers for `left` and `right` arrays

    # Step 1: Compare elements from both halves and pick the smallest one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1  # Move pointer in the left array
        else:
            sorted_array.append(right[j])
            j += 1  # Move pointer in the right array

    # Step 2: Add any remaining elements from the left array (if any)
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # Step 3: Add any remaining elements from the right array (if any)
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array




# Test array
test_array = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", test_array)

# Sort the array using merge sort
sorted_array = merge_sort(test_array)
print("Sorted array:", sorted_array)
from time import time

#Linear Search in Python


def linearSearch():
    # Search through array sequencially
    for i in range(0, length):

        #If target is found stop search
        if (array[i] == target):
            return i
    return -1


def doubleLinearSearch():

    # Search through array sequencially
    for i in range(0, length):

        j = length - i

        #If target is found stop search
        if (array[i] == target):
            return i
        elif (array[j] == target):
            return j
    return -1


#Define array and target
array = [2, 4, 0, 1, 9]
length = len(array)

target = 1

#Begin search
start = time()
result = linearSearch()
end = time()
time = end - start

#Check if found
if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result,time)


start = time()
result = doubleLinearSearch()
end = time()
time = end - start

#Check if found
if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result,time)



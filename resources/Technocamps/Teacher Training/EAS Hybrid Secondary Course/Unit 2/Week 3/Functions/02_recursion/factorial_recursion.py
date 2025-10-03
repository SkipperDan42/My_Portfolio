# An incredibly useful (though at times difficult to grasp)
# use of functions is to use them recursively!

# This function works out the factorial of a number by
# repeatedly multiplying by a call to itself
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Call the function
print("5! is:", factorial(5))
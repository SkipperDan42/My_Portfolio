def calculate_average(numbers):
    if not numbers:
        return "List is empty"
    elif not all(isinstance(n, (int, float)) for n in numbers):
        return "List must contain only numbers"
    else:
        return sum(numbers) / len(numbers)

# Call the function
print(calculate_average([10, 20, 30, 40]))  # 25.0
print(calculate_average([]))                # "List is empty"
print(calculate_average([10, "twenty", 30])) # "List must contain only numbers"
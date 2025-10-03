import time

def calculate_interest_loop(total_value, interest_rate, months):
	
	for month in range(months):
		interest_value = total_value * interest_rate
		total_value = round(total_value + interest_value, 2)

	return total_value



def calculate_interest_recursive(start_value, interest_rate, months):
	
	# Calculate new value after 1 month interest
	interest_value = start_value * interest_rate
	new_value = round(start_value + interest_value, 2)

	# If at end of timeframe, return the last starting value
	# passed to the function
	if months == 0:
		return start_value
	
	# Return the function call to itself with 1 month less each time
	return calculate_interest_recursive(new_value, interest_rate, months - 1)



# Print the results
start_time = time.time()
print(calculate_interest_loop(1000, 0.05, 100))
print(f"Calulation with a loop took {time.time() - start_time} seconds.")

start_time = time.time()
print(calculate_interest_recursive(1000, 0.05, 100))
print(f"Recursive calulation took {time.time() - start_time} seconds.")
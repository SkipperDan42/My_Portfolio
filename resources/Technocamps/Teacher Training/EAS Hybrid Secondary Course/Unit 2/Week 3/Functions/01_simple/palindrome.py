def is_palindrome(word):
    # Remove spaces and convert to lowercase for consistency
    cleaned_word = word.replace(" ", "").lower()
    
    # Check if the cleaned word reads the same forwards and backwards
    return cleaned_word == cleaned_word[::-1]

# Call the function
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
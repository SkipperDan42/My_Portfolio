def word_count(sentence):
    words = sentence.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

# Call the function
print(word_count("this is a test this is only a test"))  
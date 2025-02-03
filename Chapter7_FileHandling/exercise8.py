# Write a Python program that:
#   Count the frequency of each word in a file.

# Read the file content
with open('/Users/pulastya/Desktop/file1', 'r') as file:
    content = file.read().lower()


wordList = content.split()  # Split the content to put words in a list
wordSet = set(wordList)     # Remove duplicates so that counting can be done once

# Iterate over the set to get each word and get it's count
for word in wordSet:
    print(word, ':', wordList.count(word))
# Write a Python script to:
#   1. Read the contents of a file.
#   2. Count the number of lines, words, and characters in the file.

file = open('/Users/pulastya/Desktop/file1', 'r')
content = file.read()
num_of_line = len(content.split('\n'))
num_of_word = len(content.split())
num_of_chars = len(content)
print(f'Lines: {num_of_line}, Words: {num_of_word}, Characters: {num_of_chars}')

file.close()
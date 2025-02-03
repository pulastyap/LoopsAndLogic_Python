# Write a Python script that:
#   Asks the user for a word to search.
#   Reads a file and checks if the word exists.
#   Prints the line numbers where the word is found.

word = input('Enter the word which you want to search: ')
linenum = 0
file = open('/Users/pulastya/Desktop/file1', 'r')
for line in file.readlines():
    linenum += 1
    if word in line:
        print(f'The word \'{word}\' present at line number {linenum}')

file.close()
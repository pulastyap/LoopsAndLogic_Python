# Write a Python program that:
#   Reads a file's content.
#   Writes the reversed content to another file.

# Read the file content
with open('/Users/pulastya/Desktop/file1', 'r') as file:
    reversedContent = file.read()[::-1]


with open('/Users/pulastya/Desktop/file2', 'w') as file:
    file.write(reversedContent)
# Write a Python program that:
#   Reads a file.
#   Removes all blank lines.
#   Writes the non-blank lines back to the file.

with open('/Users/pulastya/Desktop/file1', 'r') as file:
    lines = file.readlines()

non_blank_lines = [line for line in lines if not line.isspace()]

with open('/Users/pulastya/Desktop/file1', 'w') as file:
    file.writelines(non_blank_lines)

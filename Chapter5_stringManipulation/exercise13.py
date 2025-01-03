# Exercise 13: Write a program to find the most frequently occurring character in the string "mississippi".

word = "mississippi"

max_occur = 0
max_occur_char = ""
for char in word:
    cnt = word.count(char)
    if cnt > max_occur:
        max_occur = cnt
        max_occur_char = char

print(max_occur_char, "is present", max_occur, "times in the word\"", word, "\"")
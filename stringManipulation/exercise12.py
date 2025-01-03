# Exercise 12: Write a program to remove all vowels ('a', 'e', 'i', 'o', 'u') from the string "beautiful day".

word = "beautiful day"
vowels = ('a', 'e', 'i', 'o', 'u')

for vowel in vowels:
    word = word.replace(vowel, "")

print(word)
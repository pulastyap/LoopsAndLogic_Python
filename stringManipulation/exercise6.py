# Exercise 6: Write a program to check if a given string is a palindrome. (A palindrome reads the same forwards and backwards.)

word = input("Enter the word to check palindrome: ")
reversed_word = word[::-1]

if word == reversed_word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


    
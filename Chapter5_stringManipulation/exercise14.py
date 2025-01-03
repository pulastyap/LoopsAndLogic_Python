# Exercise 14: Write a function to check if two strings are anagrams of each other (contain the same characters in a different order).
#       Input: "listen" and "silent"
#       Output: True

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

sorted_word1 = "".join(sorted(word1))
sorted_word2 = "".join(sorted(word2))

if sorted_word2 == sorted_word1:
    print("Entered words are anagrams")
else:
    print("Entered words are not anagrams")

    
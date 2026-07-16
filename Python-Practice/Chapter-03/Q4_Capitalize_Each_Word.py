# Chapter 3 - Question 4
# Capitalize the first letter of every word without using .title()

sentence = input("Enter your sentence: ")
words = sentence.split()

new_sentence = ""

for word in words:
    first_word = word[0]
    remaining = word[1:]
    new_sentence = new_sentence + first_word.upper() + remaining.lower() + " "

print(new_sentence)
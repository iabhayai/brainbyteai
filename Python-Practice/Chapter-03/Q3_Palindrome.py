text = input("Enter your word: ")
new_text = text[ : : -1]
if text == new_text:
    print("Your word is palindrome")
else:
    print("Your word is not a palindrome")
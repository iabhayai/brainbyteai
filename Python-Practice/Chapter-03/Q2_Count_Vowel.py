def count_vowels(word):
        
    count = 0
        
    for letter in word.lower():
            
        if letter in "aeiou" :
            count = count + 1
            
    return count
result = count_vowels(input("please enter your name:"))
print(result)
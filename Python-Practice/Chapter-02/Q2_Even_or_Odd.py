# Chapter 2 - Question 2

try:
    a = int(input("Enter your number: "))

    if a % 2 == 0:
        print(f"Your number {a} is even")
    else:
        print(f"Your number {a} is odd")

except ValueError:
    print("Enter a valid number")
# Chapter 2 - Question 3

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

if a >= b and a >= c:
    print(f"Largest number is {a}")
elif b >= a and b >= c:
    print(f"Largest number is {b}")
else:
    print(f"Largest number is {c}")
print("=========================================")
print("                          FIZZBUZZ                             ")
print("=========================================")
number = int(input("Enter the number in range [1:100]: "))
if number < 1 or number > 100:
    print("Please Enter number in valid range")
elif number % 3 == 0 and number % 5 == 0:
    print(f"The number {number} is FIZZBUZZ ")
elif number % 3 == 0:
    print(f"The number {number} is FIZZ ")
elif number % 5 == 0:
    print(f"The number {number} is BUZZ ")
else:
    print(f"The number {number} is neither FIZZ nor BUZZ")

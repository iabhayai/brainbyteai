# Chapter 1 - Question 6

details = "name:Abhay,age:19,city:Titwala"

parts = details.split(",")

data = {}

for item in parts:
    key, value = item.split(":")
    data[key] = value

print(data)
marks = float(input("Please Enter your marks: "))

if marks < 0 or marks > 100:
    print("Please enter valid marks")
elif marks >= 90:
    print("Candidate has been passed with Grade A")
elif marks >= 75:
    print("Candidate has been passed with Grade B")
elif marks >= 50:
    print("Candidate has been passed with Grade C")
else:
    print("Candidate has been failed")
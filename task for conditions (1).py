# Task 3 - Conditions

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# Even or Odd check
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Simple grading system
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 50:
    print("Grade B")
else:
    print("Fail")

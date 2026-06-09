# Task 4 - Loops

# For loop (printing numbers 1 to 10)
print("For Loop:")
for i in range(1, 11):
    print(i)

# While loop
print("\nWhile Loop:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Loop through a list
fruits = ["apple", "banana", "mango", "orange"]

print("\nFruits List:")
for fruit in fruits:
    print(fruit)

# Sum of numbers using loop
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print("\nSum of numbers:", total)

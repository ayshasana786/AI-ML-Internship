# Task 2: Basic Coding
# 1. Print your details
name = "Aysha"
age = 24
course = "Data Science"
print("Name:", name)
print("Age:", age)
print("Course:", course)

# 2. Add, subtract, multiply two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)

# 3. Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 4. Find largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest number is", a)
else:
    print("Largest number is", b)

# 5. Take input and display it
name = input("Enter your name: ")
print("Welcome", name)

# Task 3: Logic Building
# 1. Check positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# 2. Find largest of 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("Largest number is", a)
elif b > a and b > c:
    print("Largest number is", b)
else:
    print("Largest number is", c)

# 3. Grade system
marks = int(input("Enter marks: "))
if marks > 90:
    print("Grade A")
elif marks >= 70 and marks <= 90:
    print("Grade B")
else:
    print("Grade C")

# Task 4: Loop Practice
# 1. Print numbers 1–20
for i in range(1, 21):
    print(i)

# 2. Print even numbers
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 3. Print sum of first N numbers
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum =", sum)

# 4. Reverse numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

# Task 5: Function Practice
# 1. Function to add two numbers
def add(a, b):
    return a + b
print(add(5, 3))

# 2. Function to check prime number
def prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print("Prime Number")
    else:
        print("Not Prime Number")
prime(7)

# 3. Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))


# Task 6: Git Integration
# Create file
# day2.py
# Git Commands
# git add .
# git commit -m "Day 2 Python basics completed"
# git push

# Bonus Task
# 1. Pattern Printing
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

# 2. Reverse a number
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number is", reverse)

# 3. Count digits in a number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print("Number of digits =", count)

# Task 2: List Practice

# 1. Create a list of 10 numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

# 2. Find sum of list elements
numbers = [1,2,3,4,5]
total = sum(numbers)
print("Sum =", total)

# 3. Find maximum number
numbers = [10,45,22,89,5]
print("Maximum =", max(numbers))

# 4. Print even numbers from list
numbers = [1,2,3,4,5,6,7,8]

for i in numbers:
    if i % 2 == 0:
        print(i)

# 5. Reverse a list
numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers)


# Task 3: Dictionary Practice

# 1. Create student dictionary
student = {
    "name": "Aysha",
    "age": 24,
    "marks": 90
}

print(student)

# 2. Update marks
student["marks"] = 95
print(student)

# 3. Add new key (grade)
student["grade"] = "A"
print(student)

# 4. Print all keys and values
print(student.keys())
print(student.values())


# Task 4: String Practice

# 1. Count number of characters
text = "Hello"
print(len(text))

# 2. Reverse a string
text = "Python"
print(text[::-1])

# 3. Check palindrome
text = input("Enter string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 4. Count vowels
text = input("Enter string: ")

count = 0

for i in text:
    if i in "aeiouAEIOU":
        count = count + 1

print("Vowels =", count)


# Task 5: Set Practice

# 1. Remove duplicates from list using set
numbers = [1,2,2,3,4,4,5]

numbers = set(numbers)

print(numbers)

# 2. Find common elements between two sets
set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1 & set2)


# Task 6: List Comprehension

# 1. Create list of squares from 1-10
squares = [x*x for x in range(1,11)]
print(squares)

# 2. Create list of even numbers from 1-20
even = [x for x in range(1,21) if x % 2 == 0]
print(even)
# Homeworks
# 1. Modify String with Underscores
# Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.
# Example
# Input: hello Output: hel_lo
# Input: assalom Output: ass_alom
# Input: abcabcabcdeabcdefabcdefg Output: abc_abc_abcd_abcd_abcdef
def modify_string(txt):
    result = []
    i = 0
    count = 0
    vowels = "aeiouAEIOU"

    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
            next_char = txt[i+1] if i+1 < len(txt) else ''
            if txt[i] in vowels or next_char == '_':
                if i+1 < len(txt) - 1:
                    result.append(txt[i+1])
                    result.append('_')
                    i += 1
                elif i+1 < len(txt):
                    result.append(txt[i+1])
                    i += 1
            else:
                if i+1 < len(txt):
                    result.append('_')
            count = 0
        i += 1

    return ''.join(result)
txt = input("So‘z kiriting: ")
natija = modify_string(txt)
print("Natija:", natija)

# 2. Integer Squares Exercise
# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
n = int(input("1 dan 20 gacha son kiriting: "))
if 1 <= n <= 20:
    for i in range(n):
        print(i**2)
else:
    print("Xato: Son 1 dan kam yoki 20 dan katta bo'lmasligi kerak.")

# 3. Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using a while loop
i = 1  
while i <= 10:
    print(i)
    i += 1 

# Exercise 2: Print the following pattern
for i in range(1, 6):  # 1 dan 5 gacha
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i += 1

# Exercise 3: Calculate sum of all numbers from 1 to a given number
# Example:
# Enter number 10
# Sum is: 55
n = int(input("Enter number: "))
total = 0
for i in range(1, n + 1):
    total += i

print("Sum is:", total)

# Exercise 4: Print multiplication table of a given number
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)

# Exercise 5: Display numbers from a list using a loop
# Given:

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 50 < num < 200 and num != 180:
        print(num)

# Exercise 6: Count the total number of digits in a number
num = int(input("Son kiriting: "))
count = 0

while num > 0:
    num = num // 10 
    count += 1      

print("Raqamlar soni:", count)

# Exercise 7: Print reverse number pattern
for i in range(5, 0, -1):     
    for j in range(i, 0, -1):  
        print(j, end=' ')
    print()                  

# Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1, -1, -1):
    print(list1[i])

# Exercise 9: Display numbers from -10 to -1 using a for loop
for i in range(-10, 0):  
    print(i)

# Exercise 10: Display message “Done” after successful loop execution
for i in range(5):
    print(i)
print("Done!")

# Exercise 11: Print all prime numbers within a range
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for number in range(start, end + 1):
    if is_prime(number):
        print(number)

# Exercise 12: Display Fibonacci series up to 10 terms
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for number in range(start, end + 1):
    if is_prime(number):
        print(number)


# Exercise 13: Find the factorial of a given number
n = int(input("Son kiriting: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# 4. Return Uncommon Elements of Lists
# Task
# Return the elements that are not common between two lists. The order of elements does not matter.
# Examples
# Input: list1 = [1, 1, 2], list2 = [2, 3, 4]
# Output: [1, 1, 3, 4]
# Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6]
# Input: list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]
# Output: [2, 2, 5]
from collections import Counter
def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    common = c1 & c2
    diff1 = c1 - common
    diff2 = c2 - common
    result = list(diff1.elements()) + list(diff2.elements())
    return result
list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(uncommon_elements(list1, list2))  # [1, 1, 3, 4]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(uncommon_elements(list1, list2))  # [1, 2, 3, 4, 5, 6]

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(uncommon_elements(list1, list2))  # [2, 2, 5]

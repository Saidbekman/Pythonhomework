#### Homework Exercises
# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name=input('Enter your name:')
year_of_birthday=int(input('Enter your birthday:'))
current_year=int(2025)
age=current_year-year_of_birthday
print(f"Hello, {name}! You are {age} years old.")

# 2. Extract Car Names
# Extract car names from the following text:
txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])

# 3. Extract Car Names
# Extract car names from the following text:
txt = 'MsaatmiazD'
print(txt[::2])
print(txt[::-2])

# 4. Extract Residence Area
# Extract the residence area from the following text:
txt = "I'am John. I am from London"
txt1=txt.split()
txt1[-1]

# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.
user_input=input("Matn kirinting:")
revaersed_string=user_input[::-1]
print("Teskari matn:",revaersed_string)

# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.
vowels = input("Matn kiriting: ")
vowel_letters = "aeiouAEIOU"
count = 0
for char in vowels:
    if char in vowel_letters:
        count += 1
print("Number of vowels:", count)

# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.
number=input("Raqam kirit:")
max_number=max(number)
print("Max number:", max_number)

# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
palindrome=input("Text:")
palindrome1=palindrome[::-1]
print(palindrome==palindrome1)

# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Gmail: ")
domain = email.split('@')[-1]
print(domain)

# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.
length = int(input("Parol uzunligini kiriting: "))
password = ''.join(random.choice(characters) for _ in range(length))
print("Random password:", password)

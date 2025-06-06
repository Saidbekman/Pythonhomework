# Python Exception Handling: Exercises, Solutions, and Practice
# Exception Handling Exercises
# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    # Foydalanuvchidan ikkita son kiritishni so'raymiz
    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("Ikkinchi sonni kiriting (0 bo'lmasligi kerak): "))
    result = a / b
    print("Natija:", result)
except ZeroDivisionError:
    print("Xatolik: Sonni nolga bo‘lish mumkin emas!")

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    user_input = input("Butun son kiriting: ")
    number = int(user_input) 
    print("Siz kiritgan son:", number)
except ValueError:
    print("Xatolik: Siz haqiqiy butun son kiritmadingiz!")

# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    filename = input("Ochmoqchi bo‘lgan fayl nomini kiriting (masalan, data.txt): ")
    with open(filename, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)
except FileNotFoundError:
    print(f"Xatolik: '{filename}' nomli fayl topilmadi!")

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    a = input("Birinchi sonni kiriting: ")
    b = input("Ikkinchi sonni kiriting: ")
    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
        raise TypeError("Faqat raqam (son) kiritishingiz kerak!")
    num1 = float(a)
    num2 = float(b)

    print("Kiritilgan sonlar:", num1, "va", num2)

except TypeError as e:
    print("Xatolik:", e)

# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    filename = input("Ochmoqchi bo‘lgan fayl nomini kiriting (masalan, secret.txt): ")
    with open(filename, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)

except PermissionError:
    print(f"Xatolik: '{filename}' faylini o‘qish uchun ruxsat etilmagan!")

# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
try:
    my_list = [10, 20, 30, 40, 50]
    index = int(input("Enter an index to access the list: "))
    print("Element at index", index, "is", my_list[index])
except IndexError:
    print("Error: The index you entered is out of range!")

# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    number = input("Iltimos, biror son kiriting: ")
    number = float(number) 
    print("Siz kiritgan son:", number)
except KeyboardInterrupt:
    print("\nXatolik: Kiritish jarayoni foydalanuvchi tomonidan bekor qilindi (Ctrl + C bosildi).")

# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    result = a / b
    print("Natija:", result)
except ArithmeticError:
    print("Xatolik: Arifmetik amalda xatolik yuz berdi (ehtimol, nolga bo'lish).")

# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    filename = input("Fayl nomini kiriting (masalan: 'data.txt'): ")
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)
except UnicodeDecodeError:
    print(f"Xatolik: '{filename}' faylini 'utf-8' kodlash bilan o‘qib bo‘lmadi. Kodlash turini tekshiring.")

# 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    my_list = [1, 2, 3, 4, 5]
    my_list.push(6)
except AttributeError:
    print("Xatolik: Siz chaqirgan metod yoki atribut mavjud emas (AttributeError).")

# Python File Input Output: Exercises, Practice, Solution
# File Input/Output Exercises
# 1. Write a Python program to read an entire text file.
file_name = 'sample.txt'
with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 2. Write a Python program to read first n lines of a file.
file_name = 'sample.txt'  # O'qiladigan fayl nomi
n = 3  # Nechta qator o'qilsin, masalan 3 ta qator

with open(file_name, 'r', encoding='utf-8') as file:
    for i in range(n):
        line = file.readline()
        if line == '':
            break
        print(line, end='') 
# 3. Write a Python program to append text to a file and display the text.
file_name = 'sample.txt' 
text_to_append = "Yangi qo'shilgan qator.\n"
with open(file_name, 'a', encoding='utf-8') as file:
    file.write(text_to_append)
with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 4. Write a Python program to read last n lines of a file.
file_name = 'sample.txt' 
n = 3 
with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines() 
for line in lines[-n:]:
    print(line, end='')  

# 5. Write a Python program to read a file line by line and store it into a list.
file_name = 'sample.txt' 
lines_list = [] 
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        lines_list.append(line.rstrip('\n')) 
print(lines_list)

# 6. Write a Python program to read a file line by line and store it into a variable.
file_name = 'sample.txt'
with open(file_name, 'r', encoding='utf-8') as file:
    lines_variable = file.readlines()
print(lines_variable)

# 7. Write a Python program to read a file line by line and store it into an array.
file_name = 'sample.txt'
lines_array = []
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        lines_array.append(line.rstrip('\n')) 
print(lines_array)

# 8. Write a Python program to find the longest words.
file_name = 'sample.txt'  # Fayl nomi

# Faylni o'qib, matndagi eng uzun so'z(lar)ni topamiz
with open(file_name, 'r', encoding='utf-8') as file:
    words = file.read().split()  
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Eng uzun so'z(lar):", longest_words)
print("Uzunligi:", max_length)

# 9. Write a Python program to count the number of lines in a text file.
file_name = 'sample.txt' 
with open(file_name, 'r', encoding='utf-8') as file:
    line_count = sum(1 for line in file)
print("Fayldagi qatorlar soni:", line_count)

# 10. Write a Python program to count the frequency of words in a file.
file_name = 'sample.txt' 
word_count = {}
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        words = line.split()  
        for word in words:
            word = word.lower()  
            word_count[word] = word_count.get(word, 0) + 1
for word, count in word_count.items():
    print(f"'{word}': {count} marta")

# 11. Write a Python program to get the file size of a plain file.
import os
file_name = 'sample.txt' 
file_size = os.path.getsize(file_name)
print(f"The size of '{file_name}' is: {file_size} bytes")
print(f"File size: {file_size/1024:.2f} KB")

# 12. Write a Python program to write a list to a file.
my_list = ['apple', 'banana', 'cherry', 'date'] 
file_name = 'output.txt'
with open(file_name, 'w', encoding='utf-8') as file:
    for item in my_list:
        file.write(item + '\n')  
print(f"Ro'yxat '{file_name}' fayliga yozildi!")

# 13. Write a Python program to copy the contents of a file to another file.
source_file = 'source.txt'    
destination_file = 'copy.txt'   
with open(source_file, 'r', encoding='utf-8') as src:
    content = src.read() 
with open(destination_file, 'w', encoding='utf-8') as dst:
    dst.write(content)
print(f"{source_file} fayldagi matn {destination_file} fayliga nusxalandi!")

# 14. Write a Python program to combine each line from the first file with the corresponding line in the second file.
file1 = 'file1.txt'
file2 = 'file2.txt'
output_file = 'combined.txt'
with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(output_file, 'w', encoding='utf-8') as out:
    for line1, line2 in zip(f1, f2):
        combined_line = line1.rstrip('\n') + line2 
        out.write(combined_line)
print(f"Lines from '{file1}' and '{file2}' have been combined in '{output_file}'")

# 15. Write a Python program to read a random line from a file.
import random
file_name = 'sample.txt'
with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines() 
random_line = random.choice(lines) 
print("Tasodifiy qator:", random_line.strip())

# 16. Write a Python program to assess if a file is closed or not.
file_name = 'sample.txt'
file = open(file_name, 'r', encoding='utf-8') 
print("Fayl ochiqmi?", not file.closed)  
file.close() 
print("Fayl ochiqmi?", not file.closed)  
print("Fayl yopildimi?", file.closed)    

# 17. Write a Python program to remove newline characters from a file.
input_file = 'input.txt'       
output_file = 'output.txt'    
with open(input_file, 'r', encoding='utf-8') as infile:
    content = infile.read()        
content_no_newlines = content.replace('\n', '')  
with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write(content_no_newlines)     
print(f"Newline belgilarisiz matn '{output_file}' faylga yozildi!")

# 18. Write a Python program that takes a text file as input and returns the number of words in a given text file.
# Note: Some words can be separated by a comma with no space.
import re
file_name = 'sample.txt' 
with open(file_name, 'r', encoding='utf-8') as file:
    text = file.read()
words = re.split(r'[,\s]+', text.strip()) 
words = [word for word in words if word]
print("So'zlar soni:", len(words))

# 19. Write a Python program to extract characters from various text files and put them into a list.
file_list = ['file1.txt', 'file2.txt', 'file3.txt']
char_list = [] 
for file_name in file_list:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        for char in content:
            char_list.append(char)
print(char_list)

# 20 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string
for letter in string.ascii_uppercase:  
    file_name = f"{letter}.txt"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"This is file {file_name}\n")  
print("A.txt dan Z.txt gacha bo'lgan fayllar yaratildi!")

# 21. Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.
import string
letters_per_line = 5           
alphabet = string.ascii_uppercase 
file_name = 'alphabet.txt'
with open(file_name, 'w', encoding='utf-8') as file:
    for i in range(0, len(alphabet), letters_per_line):
        line = alphabet[i:i+letters_per_line]   
        file.write(line + '\n')                 
print(f"Barcha harflar {letters_per_line} tadan '{file_name}' fayliga yozildi!")

# # Homework:
# 1. Create your own virtual environment and install some python packages.
# cd path/to/your/folder
# mkdir myproject
# cd myproject
# python -m venv venv
# venv\Scripts\activate
# source venv/bin/activate
# pip install requests pandas
# pip install numpy matplotlib
# pip list
# deactivate

# 2. Create custom modules.
# Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
# Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)
# math_operations.py
def add(a, b):
    """Ikki sonni qo'shish."""
    return a + b

def subtract(a, b):
    """Ikki sondan ayirish."""
    return a - b

def multiply(a, b):
    """Ikki sonni ko'paytirish."""
    return a * b

def divide(a, b):
    """Ikki sonni bo'lish. Nolga bo'lishdan saqlaydi."""
    if b == 0:
        raise ValueError("Nolga bo'lish mumkin emas!")
    return a / b
# string_utils.py

def reverse_string(s):
    """Matnni teskari qiladi."""
    return s[::-1]

def count_vowels(s):
    """Matndagi unli harflar sonini hisoblaydi."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
# main.py

import math_operations
import string_utils

print(math_operations.add(3, 4))         # Natija: 7
print(math_operations.divide(8, 2))      # Natija: 4.0

print(string_utils.reverse_string("python"))  # Natija: 'nohtyp'
print(string_utils.count_vowels("Hello World"))  # Natija: 3

# 3. Create custom packages.
# Create geometry package.
#  geometry\
#      __init__.py
#      circle.py
 
# Define calculate_area and calculate_circumference functions in circle.py. These functions accept one argument(radius).
# Create file_operations package.
#  file_operations\
#      __init__.py
#      file_reader.py
#      file_writer.py
 
# Define read_file function in file_reader.py. This function accepts one argument(file_path). Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).
# geometry/circle.py

import math

def calculate_area(radius):
    """Aylananing yuzasini hisoblaydi."""
    return math.pi * radius * radius

def calculate_circumference(radius):
    """Aylananing uzunligini (perimetri) hisoblaydi."""
    return 2 * math.pi * radius
# geometry/__init__.py

from .circle import calculate_area, calculate_circumference
file_operations/
    __init__.py
    file_reader.py
    file_writer.py
# file_operations/file_reader.py

def read_file(file_path):
    """Faylni o‘qiydi va matn ko‘rinishida qaytaradi."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
# file_operations/file_writer.py

def write_file(file_path, content):
    """Matnni faylga yozadi (ustidan yozadi)."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
# file_operations/__init__.py

from .file_reader import read_file
from .file_writer import write_file
# main.py

from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

# Geometry
r = 5
print("Area:", calculate_area(r))             
print("Circumference:", calculate_circumference(r))   

# File operations
write_file("test.txt", "Hello, Python Packages!")
print(read_file("test.txt"))                  

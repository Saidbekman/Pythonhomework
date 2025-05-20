# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.
fruits=['apple', 'banana', 'orange', 'mango', 'watermelon']
print(fruits[2])

# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.
num1=[124563]
num2=[645616]
print(num1+num2)

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
list_number = [4, 5, 8, 6, 21, 49, 2107, 9, 20, 7]
first = list_number[0]
middle_index = len(list_number) // 2
middle = list_number[middle_index]
last = list_number[-1]
new_list = [first, middle, last]
print(new_list)

# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.
a = 'Sevimli oy'
b = 'Hayrli tong'
c = 'Kechagi kun'
d = 'Bolmagur bola'
e = 'Kechagi osmon'

movies_list = [a, b, c, d, e]
print(movies_list)

# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["Tashkent", "New York", "London", "Paris", "Moscow", "Berlin"]
if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")

# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.
numbers = [1, 2, 3, 4, 5]
duplicated_list = numbers * 2
print(duplicated_list)

# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.
list_number1=[4,5,8,6,21,49,2107,9,20,7]
list_number1[0],list_number1[-1]=list_number1[-1],list_number1[0]
print(list_number1)

# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
ten_list=[1,2,3,4,5,6,7,8,9,10]
print(ten_list[3:8])

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.
colors = ["red", "blue", "green", "blue", "yellow", "blue", "black"]
blue_count = colors.count("blue")
print("Number of times 'blue' appears:", blue_count)

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".
animals = ("cat", "dog", "lion", "tiger", "elephant")
lion_index = animals.index("lion")
print("Index of 'lion':", lion_index)

# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged tuple:", merged_tuple)

# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.
my_list = [10, 20, 30, 40, 50]
my_tuple = (100, 200, 300, 400)
print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.
numbers_tuple = (5, 10, 15, 20, 25)
numbers_list = list(numbers_tuple)
print("Tuple:", numbers_tuple)
print("List:", numbers_list)

# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.
numbers = (12, 45, 7, 98, 23, 56)
max_number = max(numbers)
min_number = min(numbers)
print("Maximum value:", max_number)
print("Minimum value:", min_number)

# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.
words = ("apple", "banana", "orange", "mango", "grape")
reversed_words = words[::-1]
print("Reversed tuple:", reversed_words)

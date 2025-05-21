# Python Dictionary and Set Exercises
# Dictionary Exercises
# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.
sort_dict={'first':5, 'second':3, 'third':9, 'firht':2, 'fifth': 1, 'sixth': 2}
ascending = dict(sorted(sort_dict.items(), key=lambda item: item[1]))
print("Ascending:", ascending)

# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.
# Sample Dictionary:
# {0: 10, 1: 20}
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)

# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionaries:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
all_dic = {}
all_dic.update(dic1)
all_dic.update(dic2)
all_dic.update(dic3)
print(all_dic)

# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary (n = 5):
n = 5 
squares = {}
for x in range(1, n+1):
    squares[x] = x*x
print(squares)

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
squares = {}
for x in range(1, 16): 
    squares[x] = x * x
print(squares)

# Set Exercises
# 1. Create a Set
# Write a Python program to create a set.
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. Iterate Over a Set
# Write a Python program to iterate over sets.
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)

# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)

# 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.
my_set = {1, 2, 3, 4, 5}
item_to_remove = 3 
my_set.discard(item_to_remove)
print(my_set)

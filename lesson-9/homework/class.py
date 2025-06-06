# Homework:
# Object-Oriented Programming (OOP) Exercises
# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius
c = Circle(5)
print("Radius:", c.radius)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

# 2. Person Class
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.
from datetime import datetime
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        # date_of_birth expected as 'YYYY-MM-DD' string
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        # If birth date hasn't occurred yet this year, subtract 1
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
person1 = Person("Saidbek", "Uzbekistan", "1998-06-06")
print("Ismi:", person1.name)
print("Davlati:", person1.country)
print("Tug‘ilgan sanasi:", person1.date_of_birth.strftime('%Y-%m-%d'))
print("Yoshi:", person1.calculate_age())

# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b
calc = Calculator()
print("Add:       ", calc.add(10, 5))
print("Subtract:  ", calc.subtract(10, 5))
print("Multiply:  ", calc.multiply(10, 5))
print("Divide:    ", calc.divide(10, 5))
print("Divide by zero:", calc.divide(10, 0))

# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method")
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter method")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c
circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())
square = Square(4)
print("Square area:", square.area())
print("Square perimeter:", square.perimeter())
triangle = Triangle(3, 4, 5)
print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())

# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    def search(self, value):
        return self._search(self.root, value)
    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:  # value > node.value
            return self._search(node.right, value)
bst = BinarySearchTree()
for v in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    bst.insert(v)
print(bst.search(6)) 
print(bst.search(13)) 
print(bst.search(2))   

# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element:", stack.peek())  
print("Popped:", stack.pop())       
print("Popped:", stack.pop())        
print("Is empty?", stack.is_empty())  
print("Popped:", stack.pop())        
print("Is empty?", stack.is_empty())  
print("Popped from empty stack:", stack.pop())  

# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        current = self.head
        prev = None
        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  
            prev = current
            current = current.next
        return False  
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()     
ll.delete(20)
ll.display()         
ll.delete(40)        
ll.display()         

# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name][1] += quantity
        else:
            self.items[name] = [price, quantity]

    def remove_item(self, name, quantity=1):
        if name in self.items:
            if self.items[name][1] > quantity:
                self.items[name][1] -= quantity
            else:
                del self.items[name]
        else:
            print(f"{name} is not in the cart.")

    def total_price(self):
        total = 0
        for price, quantity in self.items.values():
            total += price * quantity
        return total

    def show_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
            return
        print("Items in your cart:")
        for name, (price, quantity) in self.items.items():
            print(f"{name}: {quantity} x ${price} = ${price * quantity}")
        print(f"Total price: ${self.total_price()}")
cart = ShoppingCart()
cart.add_item("Apple", 2.5, 3)
cart.add_item("Banana", 1.2, 5)
cart.add_item("Milk", 3.0)
cart.show_cart()

cart.remove_item("Banana", 2)
cart.show_cart()

cart.remove_item("Apple", 3)
cart.show_cart()

# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Nothing to pop.")
            return None
        popped_item = self.items.pop()
        print(f"Popped: {popped_item}")
        return popped_item

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack elements (top to bottom):")
            for item in reversed(self.items):
                print(item)
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.pop()
stack.display()

# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Nothing to dequeue.")
            return None
        dequeued_item = self.items.pop(0)
        print(f"Dequeued: {dequeued_item}")
        return dequeued_item

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue elements (front to rear):")
            for item in self.items:
                print(item)
queue = Queue()
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)
queue.display()
queue.dequeue()
queue.display()
queue.dequeue()
queue.dequeue()
queue.display()

# 11. Bank Class
# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

class Bank:
    def __init__(self):
        self.customers = {}

    def add_account(self, name, initial_balance=0):
        if name in self.customers:
            print(f"Account for {name} already exists.")
        else:
            self.customers[name] = Customer(name, initial_balance)
            print(f"Account created for {name} with balance ${initial_balance}")

    def deposit(self, name, amount):
        if name in self.customers:
            self.customers[name].balance += amount
            print(f"Deposited ${amount} to {name}'s account.")
        else:
            print(f"Account for {name} does not exist.")

    def withdraw(self, name, amount):
        if name in self.customers:
            if self.customers[name].balance >= amount:
                self.customers[name].balance -= amount
                print(f"Withdrew ${amount} from {name}'s account.")
            else:
                print(f"Insufficient funds for {name}.")
        else:
            print(f"Account for {name} does not exist.")

    def show_balance(self, name):
        if name in self.customers:
            print(f"{name}'s balance: ${self.customers[name].balance}")
        else:
            print(f"Account for {name} does not exist.")

    def show_all_accounts(self):
        if not self.customers:
            print("No accounts in the bank.")
        else:
            print("Bank Accounts:")
            for name, customer in self.customers.items():
                print(f"{name}: ${customer.balance}")
bank = Bank()
bank.add_account("Alice", 500)
bank.add_account("Bob")
bank.deposit("Alice", 200)
bank.withdraw("Alice", 100)
bank.show_balance("Alice")
bank.deposit("Bob", 50)
bank.withdraw("Bob", 100)
bank.show_all_accounts()

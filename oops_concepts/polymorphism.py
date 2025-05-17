# In Python, polymorphism allows objects of different classes to be treated as objects of a common superclass, especially when they share a method or behavior, even if the implementations differ.

"""
Polymorphism in Python can be classified into four types:
  1. Duck Typing
  2. Method Overriding
  3. Operator Overloading
  4. Polymorphism with Functions and Classes
"""

# 1. Duck Typing (Pythonic Polymorphism)
class Dog:
  def speak(self):
    return "Woof!"
  
class Cat:
  def speak(self):
    return "Meow!"
  
def make_animal_speak(animal):
  print(animal.speak())

make_animal_speak(Dog())
make_animal_speak(Cat())

# 2. Method Overriding (Inheritance-Based Polymorphism)
class Vehicle:
  def start(self):
    print("Starting vehicle...")

class Car(Vehicle):
  def start(self):
    print("Starting car engine...")

class Bike(Vehicle):
  def start(self):
    print("Starting bike engine...")

for v in [Car(), Bike()]:
  v.start()

# 3. Operator Overloading - Python allows you to change the behavior of built-in operators for custom classes.
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)
  
  def __str__(self):
    return f"({self.x}, {self.y})"
  
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  

# 4. Polymorphism with Functions and Classes
class Circle:
  def area(self):
    return 3.14 * 5 * 5
  
class Square:
  def area(self):
    return 4 * 4
  
def print_area(shape):
  print(shape.area())

print_area(Circle())
print_area(Square())

# Real world example
class Payment:
  def pay(self, amount):
    pass

class CreditCardPayment(Payment):
  def pay(self, amount):
    print(f"Paid {amount} using Credit Card")

class PayPalPayment(Payment):
  def pay(self, amount):
    print(f"Paid {amount} using PayPal")

payments = [CreditCardPayment(), PayPalPayment()]
for payment in payments:
  payment.pay(100.50)

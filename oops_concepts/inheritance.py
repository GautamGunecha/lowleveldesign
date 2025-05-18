# Inheritance in Django refers to the ability of one class (typically a model, form, or view) to inherit the properties and methods of another class, just like standard Python OOP inheritance.

"""
What is Inheritance?
Inheritance is a mechanism where a child class derives properties and behaviors from a parent class. The child class can:
  Use the attributes and methods of the parent class
  Override parent class methods to provide a specific implementation
  Add its own additional attributes and methods
"""

"""
Key Benefits of Inheritance
  Code Reusability: Avoids code duplication by reusing attributes and methods of the parent class.
  Improves Maintainability: Reduces redundancy, making code easier to manage.
  Enhances Extensibility: New functionality can be added easily without modifying existing code.
"""

# How to Implement Inheritance in Python

# Step 1: Create a Parent Class
# The parent class contains common attributes and methods.

class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print(f"{self.name} is eating...")


# Step 2: Create a Child Class using Parent Class
# The child class inherits the properties and methods of the parent class.

class Dog(Animal):
  def bark(self):
    print(f"{self.name} is barking...")

# Step 3: Use the Child Class
# Using the child class

if __name__ == "__main__":
  my_dog = Dog("Buddy")
  my_dog.eat()
  my_dog.bark()


"""
Types of Inheritance in Python.
  Single Inheritance: One child class inherits from one parent class
  Multiple Inheritance: One child class inherits from multiple parent classes
  Multilevel Inheritance: Inheritance in a chain (Child → Parent → Grandparent)
  Hierarchical Inheritance: Multiple child classes inherit from the same parent class
  Hybrid Inheritance: Combination of two or more types of inheritance
"""

# Multiple Inheritance
class Father:
  def skills(self):
    print("Gardening, Programming")

class Mother:
  def skills(self):
    print("Cooking, Art")

class Child(Father, Mother):
  pass

c = Child()
c.skills() # Output: Gardening, Programming (method from first parent - MRO)
# Python uses Method Resolution Order (MRO) to determine which method to call when there are name conflicts.

# Multilevel Inheritance
class Grandparent:
  def legacy(self):
    print("Family legacy")

class Parent(Grandparent):
  def advice(self):
    print("Work hard")

class Children(Parent):
  def dream(self):
    print("Be a creator")

c = Children()
c.legacy()
c.advice()
c.dream()

# Hierarchical Inheritance
class Vehicle:
  def start(self):
    print("Vehicle starting...")

class Car(Vehicle):
  pass

class Bike(Vehicle):
  pass

car = Car()
bike = Bike()
car.start()
bike.start()

# Real-World Example: Employee Management System
class Employee:
  def __init__(self, name, salary, position):
    self.name = name
    self.salary = salary
    self.position = position
  
  def display_details(self):
    print(f"Employee: {self.name}, Salary: {self.salary}, Position: {self.position}")

class Manager(Employee):
  def __init__(self, name, salary, position, bonus):
    self.bonus = bonus
    super().__init__(name, salary, position)
  
  def display_details(self):
    super().display_details()
    print(f"Bonus: {self.bonus}")

if __name__ == "__main__":
  manager = Manager("Alice", 70000, "Software Engineer",10000)
  manager.display_details()

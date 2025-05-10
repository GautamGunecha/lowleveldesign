# In Python, classes and objects are fundamental to object-oriented programming (OOP). Here’s a detailed explanation:

# classes and objects

"""
1. What is a Class in Python?

A class is a blueprint or template for creating objects. It defines the structure and behavior (data and methods) that the objects created from the class will have.

Example
"""

class Dog:
  # Constructor (initializer method)
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
  
  def bark(self):
    return f"{self.name} says Woof!"
  

"""
2. What is an Object in Python?

An object is an instance of a class. When a class is defined, only the description for the object is defined. Memory is allocated only when an object is instantiated.

Example
"""

# Here, dog1 and dog2 are objects (instances) of the Dog class.
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Charlie", "Labrador")

# Accessing Object Methods and Attributes:
print(dog1.name)
print(dog1.bark())

"""
3. Components of a Class

__init__(): The constructor method, called when a new object is created. Initializes object attributes.
self: Refers to the instance of the class. Used to access attributes and methods.
Attributes: Variables that belong to the object (instance variables).
Methods: Functions that are defined inside a class and can operate on object data.

"""

"""
4. Advantages of Using Classes and Objects
	•	Encapsulation: Keeps data and behavior together.
	•	Reusability: Code can be reused via object instantiation.
	•	Abstraction: Hides complex implementation details.
	•	Inheritance & Polymorphism: Enables powerful design patterns and code organization.
"""

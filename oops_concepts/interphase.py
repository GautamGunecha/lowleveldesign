# In Python, the concept of interfaces is not built into the language in the same strict way as in languages like Java or C#. However, interfaces can still be defined and enforced using abstract base classes (ABCs) from the abc module.

"""
An interface is a contract that defines a set of methods that must be implemented by any class that claims to implement the interface. It does not contain implementation, only method signatures.

In Python, interfaces are usually created using abstract base classes, where:
	•	Abstract methods are methods that are declared but not implemented.
	•	Any class that inherits from an abstract base class must implement all abstract methods, or it remains abstract itself.
"""

"""
Creating an Interface Using abc.ABC

Step-by-step:
	1.	Import ABC and abstractmethod from the abc module.
	2.	Create a class that inherits from ABC.
	3.	Use the @abstractmethod decorator to declare interface methods.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

# Here, Shape is an interface with two abstract methods: area() and perimeter().

class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)

"""
	•	Rectangle implements the Shape interface by providing definitions for both area() and perimeter().
	•	If even one method was missing, Python would raise an error on instantiation.
"""

rect = Rectangle(10, 5)
print("Area:", rect.area())             # Output: Area: 50
print("Perimeter:", rect.perimeter())   # Output: Perimeter: 30

"""
Why Use Interfaces in Python?

Even though Python is dynamically typed and flexible, interfaces are useful for:
	•	Defining consistent APIs (especially in large projects).
	•	Enforcing method implementation in derived classes.
	•	Supporting polymorphism by allowing different classes to be used interchangeably if they implement the same interface.
"""

# Abstraction means hiding the complex implementation details and showing only the essential features of an object.

"""
Why Use Abstraction?
	•	To simplify complex systems by hiding unnecessary details.
	•	To enforce a contract for subclasses to follow.
	•	To focus on what an object does, rather than how it does it.
	•	To promote loose coupling and code reusability.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def sound(self):
    pass

  def breathe(self):
    print("Breathing...")

class Dog(Animal):
  def sound(self):
    print("Bark")
  
class Cat(Animal):
  def sound(self):
    print("Meow")

"""
Explanation:
	•	Animal is an abstract class and cannot be instantiated.
	•	sound() is an abstract method, so every subclass must implement it.
	•	breathe() is a concrete method, shared by all subclasses.
"""

dog = Dog()
dog.sound()
dog.breathe()

"""
Abstract Class vs Interface: Key Differences

Feature                   | Abstract Class                                  | Interface (ABCs)
Methods                     Can have abstract and concrete methods.	          Only abstract methods.
Fields                      Can have instance variables.	                    Should not have instance variables.
Constructor                 Can have constructors.                            Cannot have constructors.
Multiple Inheritance	      Supported.                                        Supported.
Access Modifiers	          Can have private, protected, public members.	    Methods are public by default.
"""

# Real-World Example: Payment System
class Payment:
  def __init__(self, amount):
    self.amount = amount

  @abstractmethod
  def pay(self):
    pass

class CreditCardPayment(Payment):
  def pay(self):
    print(f"Paid {self.amount} using Credit Card")

class PayPalPayment(Payment):
  def pay(self):
    print(f"Paid {self.amount} using PayPal")

payment = CreditCardPayment(150.75)
payment.pay()

payment = PayPalPayment(200.50)
payment.pay()

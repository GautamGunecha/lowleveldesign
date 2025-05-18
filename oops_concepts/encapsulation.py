# Encapsulation means wrapping the data (variables) and code (methods) together into a single unit (class). It restricts direct access to some of an object's components, which helps protect data integrity and prevents unintended modifications.

"""
Key Benefits of Encapsulation
  Data Hiding: Prevents direct access to sensitive data.
  Increased Security: Controls how data is accessed and modified.
  Improved Code Maintainability: Allows changes without affecting other parts of the code.
  Better Modularity: Organizes the code into logical components.
"""

# Example: Encapsulation with Private Variables
class BankAccount:
  def __init__(self, account_holder, balance):
    self.__account_holder = account_holder
    self.__balance = balance

  def get_balance(self):
    return self.__balance
  
  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
      print(f"Deposited: {amount}")
    else:
      print("Invalid deposit amount")

account = BankAccount("Gautam Gunecha", 100000)
print("Current Balance: ", account.get_balance())
account.deposit(150000)
print("Updated Balance: ", account.get_balance())

# Encapsulation Using Getters and Setters
# Encapsulation ensures that data cannot be directly accessed but must be retrieved or modified through methods.

class Employee:
  def __init__(self):
    self.__name = ""
    self.__age = 0

  def get_name(self):
    return self.__name
  
  def set_name(self, name):
    self.__name = name

  def get_age(self):
    return self.__age
  
  def set_age(self, age):
    self.__age = age

emp = Employee()
emp.set_name("John Doe")
emp.set_age(25)
print("Employee Name:", emp.get_name())
print("Employee Age:", emp.get_age())

# Encapsulation helps hide implementation details while exposing only necessary methods.
class Account:
  def __init__(self, balance):
    self.__balance = balance

  def __validate_withdrawal(self, amount):
    return amount > 0 and amount <= self.__balance
  
  def withdraw(self, amount):
    if self.__validate_withdrawal(amount):
      self.__balance -= amount
      print(f"Withdrawal Successful: {amount}")
    else:
      print("Insufficient balance or invalid amount")

  def get_balance(self):
    return self.__balance
  
my_account = Account(1000)
my_account.withdraw(300)
print("Remaining Balance:", my_account.get_balance())

"""
Encapsulation is used in many real-world applications such as:
  Banking Systems - Ensuring account details are private.
  Healthcare Applications - Protecting patient records.
  E-Commerce Platforms - Hiding payment processing details.
"""

class PaymentProcessor:
  def __init__(self, card_number, amount):
    self.__card_number = self.__mask_card_number(card_number)
    self.__amount = amount

  def __mask_card_number(self, card_number):
    return "****-****-****-" + card_number[-4:]
  
  def process_payment(self):
    print(f"Processing payment of {self.__amount} for card {self.__card_number}")

payment = PaymentProcessor("1234567812345678", 250.00)
payment.process_payment()

"""
Why Use Encapsulation in Payment Processing?
  Protects sensitive data (e.g., credit card numbers).
  Hides unnecessary details from users.
  Ensures secure transactions.
"""

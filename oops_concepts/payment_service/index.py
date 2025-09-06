from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Optional

# -------------------------------
# Enums for better type safety
# -------------------------------
class PaymentStatus(Enum):
  SUCCESS = "SUCCESS"
  FAILED = "FAILED"
  INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"
  INVALID_CARD = "INVALID_CARD"

class CardType(Enum):
  DEBIT = "DEBIT"
  CREDIT = "CREDIT"


# -------------------------------
# Payment Result Class
# -------------------------------
class PaymentResult:
  def __init__(self, status: PaymentStatus, message: str, remaining_balance: Optional[float] = None):
    self.status = status
    self.message = message
    self.remaining_balance = remaining_balance
    
  def is_successful(self) -> bool:
    return self.status == PaymentStatus.SUCCESS

# -------------------------------
# Abstract Payment Method Interface
# -------------------------------
class PaymentMethod(ABC):
  def __init__(self, user_name: str):
    self._user_name = self._validate_user_name(user_name)
    
  @staticmethod
  def _validate_user_name(user_name: str) -> str:
    if not user_name or not user_name.strip():
      raise ValueError("User name cannot be empty")
    return user_name.strip()
    
  @property
  def user_name(self) -> str:
    return self._user_name
    
  @abstractmethod
  def pay(self, amount: float) -> PaymentResult:
    """Process payment and return result"""
    pass
    
  @abstractmethod
  def get_display_info(self) -> str:
    """Get display information for the payment method"""
    pass
    
  def _validate_amount(self, amount: float) -> None:
    if amount <= 0:
      raise ValueError("Payment amount must be positive")


# -------------------------------
# Card Validator (Single Responsibility)
# -------------------------------
class CardValidator:
  @staticmethod
  def validate_card_number(card_number: str) -> bool:
    return len(card_number) >= 16 and card_number.isdigit()
    
  @staticmethod
  def validate_expiry_date(expiry_date: str) -> bool:
    try:
      if len(expiry_date.split("/")[-1]) == 2:
        exp_date = datetime.strptime(expiry_date, "%m/%y")
      else:
        exp_date = datetime.strptime(expiry_date, "%m/%Y")
      return exp_date > datetime.now()
    except ValueError:
      return False
    
  @staticmethod
  def validate_cvv(cvv: str) -> bool:
    return len(cvv) in [3, 4] and cvv.isdigit()

# -------------------------------
# Abstract Card Class
# -------------------------------
class Card(PaymentMethod, ABC):
  def __init__(self, user_name: str, card_number: str, expiry_date: str, cvv: str):
    super().__init__(user_name)
    self._card_number = self._validate_and_set_card_number(card_number)
    self._expiry_date = self._validate_and_set_expiry_date(expiry_date)
    self._cvv = self._validate_and_set_cvv(cvv)
    
  def _validate_and_set_card_number(self, card_number: str) -> str:
    if not CardValidator.validate_card_number(card_number):
      raise ValueError("Invalid card number. Must be at least 16 digits.")
    return card_number
    
  def _validate_and_set_expiry_date(self, expiry_date: str) -> str:
    if not CardValidator.validate_expiry_date(expiry_date):
      raise ValueError("Invalid or expired date. Use MM/YY or MM/YYYY format.")
    return expiry_date
    
  def _validate_and_set_cvv(self, cvv: str) -> str:
    if not CardValidator.validate_cvv(cvv):
      raise ValueError("Invalid CVV. Must be 3 or 4 digits.")
    return cvv
    
  def get_masked_card_number(self) -> str:
    return f"{self._card_number[:4]}-****-****-{self._card_number[-4:]}"
    
  @property
  @abstractmethod
  def card_type(self) -> CardType:
    pass
    
  def get_display_info(self) -> str:
    return f"{self.card_type.value} Card ending with {self.get_masked_card_number()}"
    
  def pay(self, amount: float) -> PaymentResult:
    try:
      self._validate_amount(amount)
      return PaymentResult(PaymentStatus.SUCCESS, f"Payment of ${amount:.2f} made via {self.get_display_info()}")
    except ValueError as e:
      return PaymentResult(PaymentStatus.FAILED, str(e))


# -------------------------------
# Concrete Card Implementations
# -------------------------------
class DebitCard(Card):
  @property
  def card_type(self) -> CardType:
    return CardType.DEBIT

class CreditCard(Card):
  @property
  def card_type(self) -> CardType:
    return CardType.CREDIT

# -------------------------------
# UPI Wallet Implementation
# -------------------------------
class UPIWallet(PaymentMethod):
  def __init__(self, user_name: str, upi_id: str, balance: float):
    super().__init__(user_name)
    self._upi_id = self._validate_upi_id(upi_id)
    self._balance = self._validate_balance(balance)
    
  def _validate_upi_id(self, upi_id: str) -> str:
    if not upi_id or '@' not in upi_id:
      raise ValueError("Invalid UPI ID format")
    return upi_id
    
  def _validate_balance(self, balance: float) -> float:
    if balance < 0:
      raise ValueError("Balance cannot be negative")
    return balance
    
  @property
  def balance(self) -> float:
    return self._balance
    
  @property
  def upi_id(self) -> str:
    return self._upi_id
    
  def get_display_info(self) -> str:
    return f"UPI Wallet ({self._upi_id})"
    
  def pay(self, amount: float) -> PaymentResult:
    try:
      self._validate_amount(amount)
            
      if amount > self._balance:
        return PaymentResult(
          PaymentStatus.INSUFFICIENT_FUNDS, 
          f"Insufficient balance. Available: ${self._balance:.2f}, Required: ${amount:.2f}"
        )
            
      self._balance -= amount
      return PaymentResult(
        PaymentStatus.SUCCESS,
        f"Payment of ${amount:.2f} made via {self.get_display_info()}",
        self._balance
      )
    
    except ValueError as e:
      return PaymentResult(PaymentStatus.FAILED, str(e))


# -------------------------------
# Payment Processor (Strategy Pattern)
# -------------------------------
class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
      self._payment_method = payment_method
    
    def set_payment_method(self, payment_method: PaymentMethod) -> None:
      self._payment_method = payment_method
    
    def process_payment(self, amount: float) -> PaymentResult:
      return self._payment_method.pay(amount)

# -------------------------------
# Payment Service (Facade Pattern)
# -------------------------------
class PaymentService:
  def __init__(self):
    self._processor = PaymentProcessor(None)
    
  def make_payment(self, payment_method: PaymentMethod, amount: float) -> bool:
    """Make payment and handle logging"""
    self._processor.set_payment_method(payment_method)
    result = self._processor.process_payment(amount)
        
    self._log_payment_result(result)
    return result.is_successful()
    
  def _log_payment_result(self, result: PaymentResult) -> None:
    """Log payment result with appropriate formatting"""
    status_icon = "✅" if result.is_successful() else "❌"
    print(f"{status_icon} {result.message}")
        
    if result.remaining_balance is not None:
      print(f"   Remaining balance: ${result.remaining_balance:.2f}")
        
    if result.is_successful():
      print("---- Payment Successful ----\n")
    else:
      print("---- Payment Failed ----\n")

# -------------------------------
# Client Code
# -------------------------------
def main():
  try:
    debit = DebitCard("Gautam Gunecha", "5723878987877657", "12/2035", "444")
    credit = CreditCard("Gautam Gunecha", "4895739283746257", "11/2030", "123")
    wallet = UPIWallet("Gautam Gunecha", "gautam@upi", 2000.0)
        
    payment_service = PaymentService()
        
    print("Processing payments...\n")
        
    payment_service.make_payment(debit, 500.0)
    payment_service.make_payment(credit, 1000.0)
    payment_service.make_payment(wallet, 1500.0)
    payment_service.make_payment(wallet, 600.0)
        
  except Exception as e:
    print(f"❌ Error creating payment methods: {e}")

if __name__ == "__main__":
  main()

from abc import ABC, abstractmethod

from strategies.payment.paymentStrategy import PaymentFactory
class PaymentOptionStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method")
    
class CreditCardPaymentOption(PaymentOptionStrategy):
    def __init__(self, card_number=None, expiry_date=None, cvv=None):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self, amount):
        # Logic to process credit card payment
        print(f"Processing credit card payment of {amount} using card number {self.card_number}")
        return True  # Simulate successful payment
  
class MobilePaymentOption(PaymentOptionStrategy):
    def __init__( self, mobile_number=None):
        self.mobile_number = mobile_number

    def process_payment(self, amount):
        # Logic to process mobile payment
        print(f"Processing mobile payment of {amount} using mobile number {self.mobile_number}")
        return True  # Simulate successful payment
  
class CashPaymentOption(PaymentOptionStrategy):
    def __init__(self, cash_amount=None):
        self.cash_amount = cash_amount

    def process_payment(self, amount):
        # Logic to process cash payment
        print(f"Processing cash payment of {amount}")
        return True  # Simulate successful payment
    
PaymentFactory.register_payment_strategy("credit_card", CreditCardPaymentOption)
PaymentFactory.register_payment_strategy("mobile", MobilePaymentOption)
PaymentFactory.register_payment_strategy("cash", CashPaymentOption)


class Payment:
    def __init__(self, credit_card_no=None, expiry_date=None, cvv=None, upi_id=None, mobile_number=None):
        pass

    def pay_via_credit_card(self, amount, credit_card_no, expiry_date, cvv):
        # Logic to process credit card payment
        print(f"Processing credit card payment of {amount} using card number {credit_card_no}")

        return True  # Simulate successful payment

    def pay_via_mobile(self, amount, mobile_number):
        # Logic to process mobile payment
        print(f"Processing mobile payment of {amount} using mobile number {mobile_number}")
        return True  # Simulate successful payment

    def pay_via_cash(self, amount):
        # Logic to process cash payment
        print(f"Processing cash payment of {amount}")
        return True  # Simulate successful payment
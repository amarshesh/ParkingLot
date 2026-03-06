class PaymentFactory:
    __registry = {}

    @classmethod
    def register_payment_strategy(cls, payment_method, strategy_class):
        cls.__registry[payment_method] = strategy_class
    
    @classmethod
    def get_payment_strategy(cls, payment_method):
        strategy_class = cls.__registry.get(payment_method)
        if strategy_class is None:
            raise ValueError(f"No payment strategy found for method: {payment_method}")
        return strategy_class()


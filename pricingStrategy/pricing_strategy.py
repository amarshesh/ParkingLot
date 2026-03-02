from abc import ABC, abstractmethod

# this is an starategy pattern, we can have different pricing strategies like discount, premium, etc.
class PricingStrategy( ABC):
    @abstractmethod
    def calculate_price(self, base_price):
        pass
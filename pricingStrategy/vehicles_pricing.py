
from pricingStrategy.pricing_strategy import PricingStrategy

class SmallPricing( PricingStrategy ):
    def calculate_price( self, base_price ):
        return base_price * 1.2
    
class MediumPricing( PricingStrategy ):
    def calculate_price( self, base_price ):
        return base_price * 0.8
    

class LargePricing( PricingStrategy ):
    def calculate_price( self, base_price ):
        return base_price * 1.5
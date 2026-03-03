from pricingStrategy.vehicles_pricing import LargePricing, MediumPricing, SmallPricing
class VehiclePricingFactory:
    @staticmethod
    def get_pricing_strategy(vehicle_type):
        if vehicle_type == "small":
            return SmallPricing()
        elif vehicle_type == "medium":
            return MediumPricing()
        elif vehicle_type == "large":
            return LargePricing()
        else:
            raise ValueError("Unknown vehicle type: " + vehicle_type)
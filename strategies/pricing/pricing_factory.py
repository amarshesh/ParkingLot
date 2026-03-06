class VehiclePricingFactory:
    _registry = {}
    @classmethod
    def register_pricing_strategy(cls, vehicle_size, strategy_cls):
        cls._registry[vehicle_size] = strategy_cls

    @classmethod
    def get_pricing_strategy(cls, vehicle_size):
        strategy_cls = cls._registry.get(vehicle_size)
        if strategy_cls:
            return strategy_cls()
        raise ValueError(f"No pricing strategy registered for vehicle size: {vehicle_size}")

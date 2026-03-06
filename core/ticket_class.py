import uuid

from strategies.pricing.pricing_strategy import PricingStrategy
class Ticket:

    def __init__ ( self, ticket_id, entry_time, spot_id, floor_id, vehicle_type, pricing_strategy : PricingStrategy):
        self.ticket_id = ticket_id
        self.entry_time = entry_time
        self.spot_assigned = spot_id
        self.floor_assigned = floor_id
        self.vehicle_type = vehicle_type
        self.pricing_strategy = pricing_strategy
        self.exit_time = None
        self.amount = None
    def close(self, exit_time, rate_per_hour=10):
        self.exit_time = exit_time
        duration_hours = max(1, int((exit_time - self.entry_time) / 3600))
        base_price = duration_hours * rate_per_hour
        self.amount = self.pricing_strategy.calculate_price(base_price)
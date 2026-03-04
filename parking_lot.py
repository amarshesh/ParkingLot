import uuid
import time
from parkingStrategy.allocationStrategy import AllocationStrategy
from parkingStrategy.parking_strategy import BestFitStrategy, NearestExitStrategy
from pricingStrategy.pricing_factory import VehiclePricingFactory
import pricingStrategy.vehicles_pricing
from spot_class import SpotClass
from ticket_class import Ticket
from vehicle_class import VehicleClass
class ParkingLot:
    def __init__(self, allocation_strategy=None):
        self.spots = []
        self.tickets = {}
        # default strategy
        self.allocation_strategy = allocation_strategy or BestFitStrategy()
        self.spots.append(SpotClass("S1", "small", 5))
        self.spots.append(SpotClass("S2", "medium", 10))
        self.spots.append(SpotClass("S3", "large", 3))
        self.spots.append(SpotClass("S4", "low", 2))

    def handle_entry(self, vehicle: VehicleClass):
        strategy = AllocationStrategy.resolve(self, vehicle)
        spot = strategy.allocate_spot(vehicle.size, self.spots)
        if spot is None:
            print("No spot available for vehicle size:", vehicle.size)
            return None
        spot.current_vehicle = vehicle.vehicle_number
        ticket_id = str(uuid.uuid4())
        entry_time = time.time()
        pricing_strategy = VehiclePricingFactory.get_pricing_strategy(vehicle.size)
        ticket = Ticket(ticket_id, entry_time, spot.spot_id, vehicle.size, pricing_strategy)
        self.tickets[ticket_id] = ticket
        return ticket_id

    def handle_exit(self, ticket_id):
        if ticket_id in self.tickets:
            ticket = self.tickets[ticket_id]
            end_time = time.time()
            ticket.close(end_time, rate_per_hour=10)
            amount = ticket.amount
            spot_id = ticket.spot_assigned
            print(f"Spot id assigned for ticket {ticket_id} is {spot_id}")
            for spot in self.spots:
                if spot.spot_id == spot_id:
                    spot.current_vehicle = None
                    break
            return amount
        return None
    

if __name__ == "__main__":
    parking_lot = ParkingLot(BestFitStrategy())

    v1 = VehicleClass("KA-01-AB-1234", "small", False, True, False)
    tid1 = parking_lot.handle_entry(v1)
    print("Ticket ID:", tid1)
    time.sleep(2)

    v2 = VehicleClass("KA-01-AB-5678", "medium", False, True, False)
    tid2 = parking_lot.handle_entry(v2)
    print("Ticket ID:", tid2)
    time.sleep(2)

    v3 = VehicleClass("KA-01-AB-9012", "large", False, True, False)
    tid3 = parking_lot.handle_entry(v3)
    print("Ticket ID:", tid3)
    time.sleep(2)

    v4 = VehicleClass("KA-01-AB-9022", "low", False, True, False)
    tid4 = parking_lot.handle_entry(v4)
    print("Ticket ID:", tid4)
    time.sleep(2)




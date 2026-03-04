import uuid
import time
from floors.floors import Floor
from parkingStrategy.allocationStrategy import AllocationStrategy
from parkingStrategy.parking_strategy import BestFitStrategy, NearestExitStrategy
from pricingStrategy.pricing_factory import VehiclePricingFactory
import pricingStrategy.vehicles_pricing
from spot_class import SpotClass
from ticket_class import Ticket
from vehicle_class import VehicleClass
class ParkingLot:
    def __init__(self, allocation_strategy=None):
        self.tickets = {}
        self.floors = []
        floor1 = Floor("Floor-1")
        for i in range(1, 5):
            spot = SpotClass(f"Spot-{i}", "small", distance_to_exit=i)
            floor1.add_spot(spot)
        for i in range(5, 11):
            spot = SpotClass(f"Spot-{i}", "medium", distance_to_exit=i)
            floor1.add_spot(spot)

        floor2 = Floor("Floor-2")
        for i in range(11, 15):
            spot = SpotClass(f"Spot-{i}", "medium", distance_to_exit=i)
            floor2.add_spot(spot)

        for i in range(15, 21):
            spot = SpotClass(f"Spot-{i}", "large", distance_to_exit=i)
            floor2.add_spot(spot)
        
        floor3 = Floor("Floor-3")
        for i in range(21, 25):
            spot = SpotClass(f"Spot-{i}", "large", distance_to_exit=i)
            floor3.add_spot(spot)

        for i in range( 25, 31):
            spot = SpotClass(f"Spot-{i}", "small", distance_to_exit=i)
            floor3.add_spot(spot)
        
        floor4 = Floor("Floor-4")
        for i in range(31, 41):
            spot = SpotClass(f"Spot-{i}", "low", distance_to_exit=i)
            floor4.add_spot(spot)
         
        floor5 = Floor("Floor-5")
        for i in range(41, 51):
            spot = SpotClass(f"Spot-{i}", "midlow", distance_to_exit=i)
            floor5.add_spot(spot)
        
        self.floors.append(floor1)
        self.floors.append(floor2) 
        self.floors.append(floor3)
        self.floors.append(floor4)
        self.floors.append(floor5)
    def handle_entry(self, vehicle: VehicleClass):
        for floor in self.floors:
            strategy = AllocationStrategy.resolve(self, vehicle=vehicle)
            allocated_spot = strategy.allocate_spot(vehicle.size, floor.spots)

            if allocated_spot is not None:
                allocated_spot.current_vehicle = vehicle

                pricing_strategy = VehiclePricingFactory.get_pricing_strategy(vehicle.size)
                ticket_id = str(uuid.uuid4())
                entry_time = time.time()

                ticket = Ticket(ticket_id, entry_time, allocated_spot.spot_id, floor.floor_id, vehicle.size, pricing_strategy)
                self.tickets[ticket_id] = ticket

                print(f"Vehicle {vehicle.vehicle_number} (size {vehicle.size}) assigned to {floor.floor_id} at spot {allocated_spot.spot_id} (spot size: {allocated_spot.size})")

                return ticket_id

        print(f"No spot available for vehicle {vehicle.vehicle_number} of size {vehicle.size}")
        return None
    def handle_exit(self, ticket_id):
        if ticket_id in self.tickets:
            ticket = self.tickets[ticket_id]
            end_time = time.time()
            ticket.close(end_time, rate_per_hour=10)
            amount = ticket.amount
            spot_id = ticket.spot_assigned
            print(f"Spot id assigned for ticket {ticket_id} is {spot_id}")
            for floor in self.floors:
                for spot in floor.spots:
                    if spot.spot_id == spot_id:
                        spot.current_vehicle = None
                        break
            return amount
        return None
    
if __name__ == "__main__":
    parking_lot = ParkingLot(BestFitStrategy())

    v1 = VehicleClass("KA-01-AB-1234", "small", False, True, False)
    tid1 = parking_lot.handle_entry(v1)
    # print("Ticket ID:", tid1)
    time.sleep(2)
    # amount = parking_lot.handle_exit(tid1)
    # print("Amount:", amount)

    v2 = VehicleClass("KA-01-AB-5678", "medium", False, False, False)
    tid2 = parking_lot.handle_entry(v2)
    # print("Ticket ID:", tid2)/
    time.sleep(2)
    # amount = parking_lot.handle_exit(tid2)
    # print("Amount:", amount)

    v3 = VehicleClass("KA-01-AB-9012", "large", False, False, False)
    tid3 = parking_lot.handle_entry(v3)
    # print("Ticket ID:", tid3)
    time.sleep(2)
    # amount = parking_lot.handle_exit(tid3)
    # print("Amount:", amount)

    v4 = VehicleClass("KA-01-AB-9022", "low", False, False, False)
    tid4 = parking_lot.handle_entry(v4)
    # print("Ticket ID:", tid4)
    time.sleep(2)
    # amount = parking_lot.handle_exit(tid4)
    # print("Amount:", amount)

    v5 = VehicleClass("KA-01-AB-9999", "midlow", False, True, False)
    tid5 = parking_lot.handle_entry(v5)
    # print("Ticket ID:", tid5)
    time.sleep(2)
    # amount = parking_lot.handle_exit(tid5)
    # print("Amount:", amount)                                                      
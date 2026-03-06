import uuid
import time
import threading

from floors.floors import Floor
from parkingStrategy.allocationStrategy import AllocationStrategy
from parkingStrategy.parking_strategy import BestFitStrategy
from paymentStrategy.paymentStrategy import PaymentFactory
from pricingStrategy.pricing_factory import VehiclePricingFactory

from spot_class import SpotClass
from ticket_class import Ticket
from vehicle_class import VehicleClass

import pricingStrategy.vehicles_pricing
import paymentStrategy.payment_options


class ParkingLot:

    def __init__(self, allocation_strategy=None):
        self.tickets = {}
        self.floors = []
        self.allocation_strategy = allocation_strategy or BestFitStrategy()
        self.lock = threading.Lock()

        # -------- Floor 1 --------
        floor1 = Floor("Floor-1")
        for i in range(1, 5):
            floor1.add_spot(SpotClass(f"Spot-{i}", "small", distance_to_exit=i))
        for i in range(5, 11):
            floor1.add_spot(SpotClass(f"Spot-{i}", "medium", distance_to_exit=i))

        # -------- Floor 2 --------
        floor2 = Floor("Floor-2")
        for i in range(11, 15):
            floor2.add_spot(SpotClass(f"Spot-{i}", "medium", distance_to_exit=i))
        for i in range(15, 21):
            floor2.add_spot(SpotClass(f"Spot-{i}", "large", distance_to_exit=i))

        # -------- Floor 3 --------
        floor3 = Floor("Floor-3")
        for i in range(21, 25):
            floor3.add_spot(SpotClass(f"Spot-{i}", "large", distance_to_exit=i))
        for i in range(25, 31):
            floor3.add_spot(SpotClass(f"Spot-{i}", "small", distance_to_exit=i))

        # -------- Floor 4 --------
        floor4 = Floor("Floor-4")
        for i in range(31, 41):
            floor4.add_spot(SpotClass(f"Spot-{i}", "low", distance_to_exit=i))

        # -------- Floor 5 --------
        floor5 = Floor("Floor-5")
        for i in range(41, 51):
            floor5.add_spot(SpotClass(f"Spot-{i}", "midlow", distance_to_exit=i))

        self.floors.extend([floor1, floor2, floor3, floor4, floor5])


    def handle_entry(self, vehicle: VehicleClass):

        with self.lock:
            time.sleep(0.5)  # Simulate processing time

            strategy = AllocationStrategy.resolve(vehicle)

            for floor in self.floors:

                allocated_spot = strategy.allocate_spot(vehicle.size, floor.spots)

                if allocated_spot:

                    allocated_spot.current_vehicle = vehicle

                    pricing_strategy = VehiclePricingFactory.get_pricing_strategy(vehicle.size)

                    ticket_id = str(uuid.uuid4())
                    entry_time = time.time()

                    ticket = Ticket(
                        ticket_id,
                        entry_time,
                        allocated_spot.spot_id,
                        floor.floor_id,
                        vehicle.size,
                        pricing_strategy
                    )

                    self.tickets[ticket_id] = ticket

                    print(
                        f"{vehicle.vehicle_number} parked at "
                        f"{floor.floor_id}-{allocated_spot.spot_id}"
                    )

                    return ticket_id

            print(f"No spot available for {vehicle.vehicle_number}")
            return None

    def handle_exit(self, ticket_id, payment_method="cash"):

        with self.lock:

            ticket = self.tickets.get(ticket_id)

            if not ticket:
                print("Invalid ticket")
                return None

            end_time = time.time()
            ticket.close(end_time, rate_per_hour=10)

            amount = ticket.amount

            print(f"Processing payment: {amount}")

            payment_strategy = PaymentFactory.get_payment_strategy(payment_method)

            payment_status = payment_strategy.process_payment(amount)

            if not payment_status:
                print("Payment failed")
                return None

            # free spot
            for floor in self.floors:
                for spot in floor.spots:
                    if spot.spot_id == ticket.spot_assigned:
                        spot.current_vehicle = None
                        break

            del self.tickets[ticket_id]

            print("Exit successful")

            return amount


# ---------------- TEST ----------------

def simulate_entry(parking_lot, vehicle):
    tid = parking_lot.handle_entry(vehicle)
    if tid:
        print(f"{vehicle.vehicle_number} → ticket {tid}")
    else:
        print(f"{vehicle.vehicle_number} → no parking")


if __name__ == "__main__":

    parking_lot = ParkingLot()

    vehicles = [
        VehicleClass(f"KA-01-AB-{1000+i}", "small", False, False, False)
        for i in range(20)
    ]

    threads = []

    for v in vehicles:
        t = threading.Thread(target=simulate_entry, args=(parking_lot, v))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Simulation finished")


       
# if __name__ == "__main__":
#     parking_lot = ParkingLot(BestFitStrategy())
#     v1 = VehicleClass("KA-01-AB-1234", "small", False, True, False)
#     tid1 = parking_lot.handle_entry(v1)
#     print("Ticket ID:", tid1)
#     time.sleep(2)
#     amount = parking_lot.handle_exit(tid1, "credit_card")
#     print("Amount:", amount)

#     v2 = VehicleClass("KA-01-AB-5678", "medium", False, False, False)
#     tid2 = parking_lot.handle_entry(v2)
#     print("Ticket ID:", tid2)
#     time.sleep(2)
#     amount = parking_lot.handle_exit(tid2, "mobile")
#     print("Amount:", amount)

#     v3 = VehicleClass("KA-01-AB-9012", "large", False, False, False)
#     tid3 = parking_lot.handle_entry(v3)
#     print("Ticket ID:", tid3)
#     time.sleep(2)
#     amount = parking_lot.handle_exit(tid3,"cash")
#     print("Amount:", amount)

#     v4 = VehicleClass("KA-01-AB-9022", "low", False, False, False)
#     tid4 = parking_lot.handle_entry(v4)
#     print("Ticket ID:", tid4)
#     time.sleep(2)
#     amount = parking_lot.handle_exit(tid4, "mobile")
#     print("Amount:", amount)

#     v5 = VehicleClass("KA-01-AB-9999", "midlow", False, True, False)
#     tid5 = parking_lot.handle_entry(v5)
#     print("Ticket ID:", tid5)
#     time.sleep(2)
#     amount = parking_lot.handle_exit(tid5, "cash")
#     print("Amount:", amount)                                                      

import uuid
import time
from pricingStrategy.pricing_factory import VehiclePricingFactory
from spot_class import SpotClass
from ticket_class import Ticket
class ParkingLot:
    def __init__(self):
        self.spots = []
        self.tickets = {}
        self.spots.append(SpotClass("S1", "small"))
        self.spots.append(SpotClass("S2", "medium"))
        self.spots.append(SpotClass("S3", "large"))

    def handle_entry(self, vehicle_number, vehicle_size):
        for spot in self.spots:
            if spot.size == vehicle_size and spot.current_vehicle is None:
                spot.current_vehicle = vehicle_number
                ticket_id = str(uuid.uuid4())
                entry_time = time.time()
                pricing_strategy = VehiclePricingFactory.get_pricing_strategy(vehicle_size)
                ticket = Ticket(ticket_id, entry_time, spot.spot_id, vehicle_size, pricing_strategy)
                self.tickets[ticket_id] = ticket    
                return ticket_id
        return None
    
    def handle_exit(self, ticket_id):
        if ticket_id in self.tickets:
            ticket = self.tickets[ticket_id]
            end_time = time.time()
            ticket.close(end_time, rate_per_hour=10)
            amount = ticket.amount
            spot_id = ticket.spot_assigned
            for spot in self.spots:
                if spot.spot_id == spot_id:
                    spot.current_vehicle = None
                    break
            return amount
        return None
    

if __name__ == "__main__":
    parking_lot = ParkingLot()

    tid1 = parking_lot.handle_entry("KA-01-AB-1234", "small")
    print("Ticket ID:", tid1)
    time.sleep(2)
    amount1 = parking_lot.handle_exit(tid1)
    print("Amount for ticket", tid1, "is", amount1)
    

    tid2 = parking_lot.handle_entry("KA-01-AB-5678", "medium")
    print("Ticket ID:", tid2)
    time.sleep(2)   
    amount2 = parking_lot.handle_exit(tid2)
    print("Amount for ticket", tid2, "is", amount2)
    

    tid3 = parking_lot.handle_entry("KA-01-AB-9012", "large")
    print("Ticket ID:", tid3)
    time.sleep(2)
    amount3 = parking_lot.handle_exit(tid3)
    print("Amount for ticket", tid3, "is", amount3)





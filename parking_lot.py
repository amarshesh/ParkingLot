import uuid
import time

class ParkingLot:

    def __init__(self, num_of_spot):
        self.total_spots = num_of_spot
        self.available_spots = num_of_spot
        self.vehicle_spot = {}          # {vehicle_number: True/False}
        self.tickets = {}               # {vehicle_number: (ticket_id, entry_time)}

    def _assign_spot(self, vehicle_number):
        if self.available_spots <= 0:
            return False
        if vehicle_number not in self.vehicle_spot:
            self.vehicle_spot[vehicle_number] = True
            self.available_spots -= 1
            print(f"Spot assigned to {vehicle_number}")
            return True
        return False

    def _create_parking_ticket(self, vehicle_number):
        if self._assign_spot(vehicle_number):
            ticket_number = uuid.uuid4().hex[:8]
            entry_time = time.time()
            self.tickets[vehicle_number] = (ticket_number, entry_time)
            print(f"Ticket created for {vehicle_number}")
            return True
        return False

    def _vacate_spot(self, vehicle_number):
        if vehicle_number in self.vehicle_spot:
            del self.vehicle_spot[vehicle_number]
            self.available_spots += 1
            print(f"Spot vacated for {vehicle_number}")
            return True
        return False

    def _handle_payment(self, vehicle_number):
        if vehicle_number in self.tickets:
            ticket_id, entry_time = self.tickets[vehicle_number]
            duration = int((time.time() - entry_time) / 3600) + 1
            amount = duration * 20
            print(f"Payment received: ₹{amount}")
            del self.tickets[vehicle_number]

    def handle_entry(self, vehicle_number):
        print(f"Handling entry for {vehicle_number}")
        self._create_parking_ticket(vehicle_number)

    def handle_exit(self, vehicle_number):
        self._handle_payment(vehicle_number)
        self._vacate_spot(vehicle_number)


# usage
parkinglot1 = ParkingLot(10)
parkinglot1.handle_entry("abcdefgh")
# wiit for 4 econd
time.sleep(4)
parkinglot1.handle_exit("abcdefgh")
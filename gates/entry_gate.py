

from parking_lot import ParkingLot
from vehicle_class import VehicleClass


class EntryGate:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot
    def process_entry(self, vehicle_number, size, emergency_vehicle, VIP_vehicle, elderly_vehicle):
        vehicle = VehicleClass(vehicle_number, size, emergency_vehicle, VIP_vehicle, elderly_vehicle)
        ticket = self.parking_lot.handle_entry(vehicle)
        return ticket
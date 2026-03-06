from gates.entry_gate import EntryGate
from gates.exit_gate import ExitGate
from core.parking_lot import ParkingLot

if __name__ == "__main__":
    parking_lot = ParkingLot()
    entry_gate = EntryGate(parking_lot)
    ticket = entry_gate.process_entry(
        "KA-01-AB-1234",
        "small",
        False,
        False,
        False
    )
    print("Ticket:", ticket.ticket_id if ticket else "No ticket issued")

    exit_gate = ExitGate(parking_lot)
    if ticket:
        exit_gate.process_exit(ticket.ticket_id, payment_method="cash")
        
class ExitGate:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    def process_exit(self, ticket_id, payment_method="cash"):
        return self.parking_lot.handle_exit(ticket_id, payment_method)
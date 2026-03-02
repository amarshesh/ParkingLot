import uuid
class Ticket:

    def __init__ ( self, ticket_id, entry_time, spot_id, vehicle_type):
        self.ticket_id = ticket_id
        self.entry_time = entry_time
        self.spot_assigned = spot_id
        self.vehicle_type = vehicle_type
        self.exit_time = None
        self.amount = None

    
    
    def close(self, exit_time, rate_per_hour):
        self.exit_time = exit_time
        duration_hours = max(1, int((exit_time - self.entry_time) / 3600))
        self.amount = duration_hours * rate_per_hour
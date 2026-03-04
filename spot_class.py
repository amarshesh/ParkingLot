
class SpotClass:
    def __init__( self, spot_id, size, distance_to_exit=10):
        self.spot_id = spot_id
        self.size = size
        self.current_vehicle = None
        self.distance_to_exit = distance_to_exit
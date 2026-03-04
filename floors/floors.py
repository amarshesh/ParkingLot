class Floor:
    def __init__( self, floor_id):
        self.floor_id = floor_id
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)
    
    def get_spot( self, spot_id):
        for spot in self.spots:
            if spot.spot_id == spot_id:
                return spot
        return None
    

class DisplayBoard:
    @staticmethod
    def show(parking_lot):
        for floor in parking_lot.floors:
            counts = {}

            for spot in floor.spots:
                if spot.current_vehicle is None:
                    counts[spot.size] = counts.get(spot.size, 0) + 1

            print(f"{floor.floor_id}: {counts}")
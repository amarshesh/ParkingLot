from abc import ABC, abstractmethod

class SpotAllocationStrategy(ABC):
    @abstractmethod
    def allocate_spot(self, vehicle_size, spots):
        pass

# now creating diffrent strategies for spot allocation 
SIZE_ORDER = {"small": 1, "medium": 2, "large": 3, "low": 0, "midlow": 0.5}
#i) here if a small vehicle can fit inside medium or large it can come... 
class BestFitStrategy(SpotAllocationStrategy):
    def allocate_spot(self, vehicle_size, spots):
        vehicle_rank = SIZE_ORDER[vehicle_size]
        for spot in spots:
            if spot.current_vehicle is None and SIZE_ORDER[spot.size] >= vehicle_rank:
                return spot
        return None
    
class NearestExitStrategy(SpotAllocationStrategy):
    def allocate_spot(self, vehicle_size, spots):
        vehicle_rank = SIZE_ORDER[vehicle_size]
        nearest_spot = None
        for spot in spots:
            if spot.current_vehicle is None and SIZE_ORDER[spot.size] >= vehicle_rank:
                if nearest_spot is None or spot.distance_to_exit < nearest_spot.distance_to_exit:
                    nearest_spot = spot
        return nearest_spot



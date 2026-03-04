from parkingStrategy.parking_strategy import NearestExitStrategy, BestFitStrategy
class AllocationStrategy:
    @staticmethod
    def resolve( self, vehicle):
        if vehicle.VIP_vehicle:
            return NearestExitStrategy()
        else:
            return BestFitStrategy()
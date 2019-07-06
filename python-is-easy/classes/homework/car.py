import typing
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        weight: int) -> None:
        Vehicle.__init__(self)
        self.isDriving: bool = False
    
    def drive(self) -> None:
        self.isDriving = True
    
    def stop(self) -> None:
        self.isDriving = False
        self._add_trip()
    
    def _add_trip(self) -> None:
        self.trips_since_maintenance += 1
        self._check_if_needs_maintenance()
    
    def _check_if_needs_maintenance(self) -> None:
        if self.trips_since_maintenance > 100:
            self.needs_maintenance = True
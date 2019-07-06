from vehicle import Vehicle

class Car(Vehicle):
    def __init__(
        self,
        make,
        model,
        year,
        weight):
        Vehicle.__init__(self)
        self.isDriving = False
    
    def drive(self):
        self.isDriving = True
    
    def stop(self):
        self.isDriving = False
        self._add_trip()
    
    def _add_trip(self):
        self.trips_since_maintenance += 1
        self._check_if_needs_maintenance()
    
    def _check_if_needs_maintenance(self):
        if self.trips_since_maintenance > 100:
            self.needs_maintenance = True
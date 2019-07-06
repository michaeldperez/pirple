import typing

class Vehicle(object):
    def __init__(
        self, 
        make: str   = None,
        model: str  = None, 
        year: int   = None,
        weight: int = None,
        needs_maintenance: bool      = False,
        trips_since_maintenance: int =  0) -> None:
        '''
            make:   manufacturer of vehicle
            model:  model of vehicle
            year:   year particular vehicle was released
            weight: weight of vehicle (in tons)
            needs_maintenance: whether vehicle requires service
            trips_since_maintenance: number or trips since vehicle was
                                     last serviced
        '''
        self.make                    = make
        self.model                   = model
        self.year                    = year
        self.weight                  = weight
        self.needs_maintenance       = needs_maintenance
        self.trips_since_maintenance = trips_since_maintenance

    def set_make(self, new_make: str) -> None:
        self.make = new_make
    
    def set_model(self, new_model: str) -> None:
        self.model = new_model
    
    def set_year(self, new_year: int) -> None:
        self.year = new_year
    
    def set_weight(self, new_weight: int) -> None:
        self.weight = new_weight

    def repair(self):
        self.needs_maintenance = False
        self.trips_since_maintenance = 0
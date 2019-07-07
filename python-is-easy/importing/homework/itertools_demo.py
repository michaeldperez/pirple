import itertools
from collections import namedtuple

ItoolsConfig = namedtuple(
    'ItoolsConfig', 
    [
        'count_start',
        'count_step',
        'cycle_iter'
    ]
)

class Itertools(object):
    '''
    class to demo *many* of the functions in the itertools module
    '''
    def __init__(self, config):
        self.config   = config
        self._counter = itertools.count(
            start = self.config.count_start,
            step  = self.config.count_step
        )
        self._cycler = itertools.cycle(self.config.cycle_iter)
    
    @property
    def counter(self):
        return self._counter
    
    def count(self, n = 1):
        return Itertools.iterate(self.counter, n)
    
    @property
    def cycler(self):
        return self._cycler
    
    def cycle(self, n = 1):
        return Itertools.iterate(self.cycler, n)
    
    @staticmethod
    def iterate(prop, n):
        for _ in range (n - 1):
            next(prop)
        return next(prop)

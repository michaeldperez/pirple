import itertools
from collections import namedtuple

ItoolsConfig = namedtuple(
    'ItoolsConfig', 
    [
        'count_start',
        'count_step',
        'cycle_iter',
        'repeat_obj'
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
        self._repeater = itertools.repeat(
            object=self.config.repeat_obj)
    
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
    
    @property
    def repeater(self):
        return self._repeater
    
    def repeat(self, n = 1):
        return Itertools.iterate(self.repeater, n)
    
    @staticmethod
    def iterate(prop, n):
        for _ in range (n - 1):
            next(prop)
        return next(prop)

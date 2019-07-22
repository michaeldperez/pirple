import itertools

class Itertools(object):
    @property
    def counter(self, start, step=1):
        return itertools.count(start, step)
    
    @property
    def cycle(self, iterable):
        return itertools.cycle(iterable)
    
    @property
    def repeat(self, object, times=None):
        return itertools.repeat(object, times)

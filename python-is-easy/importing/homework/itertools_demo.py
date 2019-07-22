import itertools

class Itertools(object):
    def counter(self, start=0, step=1):
        return itertools.count(start, step)
    
    def cycle(self, iterable):
        return itertools.cycle(iterable)
    
    def repeat(self, object, times=None):
        return itertools.repeat(object, times)

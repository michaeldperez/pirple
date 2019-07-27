import itertools

class Itertools(object):
    def count(self, start=0, step=1):
        return itertools.count(start, step)
    
    def cycle(self, iterable):
        return itertools.cycle(iterable)
    
    def repeat(self, obj, times=None):
        if times:
            return itertools.repeat(obj, times)
        return itertools.repeat(obj)

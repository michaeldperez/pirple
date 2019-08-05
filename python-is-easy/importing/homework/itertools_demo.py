import itertools
import operator

class Itertools(object):
    ''' The purpose of this class is to learn a library
        and demonstrate that knowledge through examples
        on how to use its methods. See ./test_itertools_demo.py
        for example uses in the form of tests.
    '''

    # infinte iterators
    def count(self, start=0, step=1):
        return itertools.count(start, step)
    
    def cycle(self, iterable):
        return itertools.cycle(iterable)
    
    def repeat(self, obj, times=None):
        if times:
            return itertools.repeat(obj, times)
        return itertools.repeat(obj)
    
    # combinatoric iterators
    def product(self, *args, repeat=1):
        return itertools.product(*args, repeat=repeat)
    
    def permutations(self, iterable, length=None):
        return itertools.permutations(iterable, r=length)

    def combinations(self, iterable, length):
        return itertools.combinations(iterable, length)
    
    def combinations_with_replacement(self, iterable, length):
        return itertools.combinations_with_replacement(iterable, length)
    
    # function iterators
    def accumulate(self, iterable, func=operator.add):
        return itertools.accumulate(iterable, func)
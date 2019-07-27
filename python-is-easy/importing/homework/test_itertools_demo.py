import unittest
from itertools_demo import Itertools

class TestItertools(unittest.TestCase):
    def setUp(self):
        self.itertools = Itertools()
    
    def test_counter(self):
        self.assertEqual(next(self.itertools.count()), 0)

    def test_count_n_times(self):
        counter = self.itertools.count()
        count_to_five = None
        for _ in range(5):
            count_to_five = next(counter)
        self.assertEqual(count_to_five, 4)
    
    def test_counter_step(self):
        counter = self.itertools.count(start=1, step=2)
        odds = list(next(counter) for _ in range(5))
        self.assertEqual(odds, [1,3,5,7,9])
    
    def test_cycle(self):
        cycler = self.itertools.cycle('abcd')
        cycle = list(next(cycler) for _ in range(8))
        self.assertEqual(cycle, [
            'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'
        ])
    
    def test_infinite_repeat(self):
        repeater = self.itertools.repeat(1)
        for _ in range(100):
            next(repeater)
        self.assertEqual(next(repeater), 1)
    
    def test_n_repeat(self):
        repeater = self.itertools.repeat('a', 10)
        repeat = list(next(repeater) for _ in range(10))
        self.assertEqual(repeat, [
            'a', 'a', 'a', 'a', 'a', \
            'a', 'a', 'a', 'a', 'a'
        ])




if __name__ == '__main__':
    unittest.main()
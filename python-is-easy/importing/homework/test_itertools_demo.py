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
    
    # def test_cycler(self):
    #     self.assertEqual(next(self.iter_tools.cycler), 'A')
    
    # def test_cycle_initial(self):
    #     self.assertEqual(self.iter_tools.cycle(), 'A')
    
    # def test_cycle_n_times(self):
    #     self.assertEqual(self.iter_tools.cycle(10), 'B')
    
    # def test_repeater(self):
    #     self.assertEqual(next(self.iter_tools.repeater), 'Hello')
    
    # def test_repeat(self):
    #     self.assertEqual(self.iter_tools.repeat(), 'Hello')
    
    # def test_repeat_n_times(self):
    #     self.assertEqual(self.iter_tools.repeat(10), 'Hello')



if __name__ == '__main__':
    unittest.main()
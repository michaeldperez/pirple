import unittest
from itertools_demo import ItoolsConfig, Itertools

class TestItertools(unittest.TestCase):
    def setUp(self):
        self.config = ItoolsConfig(
            count_start = 0,
            count_step  = 1,
            cycle_iter  = 'ABCD'
        )
        self.iter_tools = Itertools(self.config)
    
    def test_counter(self):
        self.assertEqual(next(self.iter_tools.counter), 0)
    
    def test_count_initial(self):
        self.assertEqual(self.iter_tools.count(), 0)
    
    def test_count_n_times(self):
        count_to_five = self.iter_tools.count(5)
        self.assertEqual(count_to_five, 4)
    
    def test_cycler(self):
        self.assertEqual(next(self.iter_tools.cycler), 'A')
    
    def test_cycle_initial(self):
        self.assertEqual(self.iter_tools.cycle(), 'A')
    
    def test_cycle_n_times(self):
        self.assertEqual(self.iter_tools.cycle(10), 'B')


if __name__ == '__main__':
    unittest.main()
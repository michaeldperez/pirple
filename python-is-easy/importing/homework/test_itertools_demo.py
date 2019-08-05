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

    def test_product(self):
        productor = self.itertools.product(
            ['a', 'b','c'], \
            ['x', 'y', 'z']
        )
        cartesian_product = list(next(productor) for _ in range(9))
        self.assertEqual(cartesian_product, [
            ('a', 'x'), ('a', 'y'), ('a', 'z'), \
            ('b', 'x'), ('b', 'y'), ('b', 'z'), \
            ('c', 'x'), ('c', 'y'), ('c', 'z')
        ])

    def test_self_product(self):
        prouctor = self.itertools.product([1, 2, 3], repeat=3)
        cartesian_product = list(next(prouctor) for _ in range(6))
        self.assertEqual(cartesian_product, [
            (1,1,1), (1,1,2), (1,1,3), \
            (1,2,1), (1,2,2), (1,2,3)
        ])

    def test_full_permutations(self):
        permut = self.itertools.permutations('abc')
        permutaitons = list(next(permut) for _ in range(6))
        self.assertEqual(permutaitons, [
            ('a', 'b', 'c'), ('a', 'c', 'b'), \
            ('b', 'a', 'c'), ('b', 'c', 'a'), \
            ('c', 'a', 'b'), ('c', 'b', 'a')
        ])

    def test_reduced_permutations(self):
        permut = self.itertools.permutations('abcd', 2)
        permutations = list(next(permut) for _ in range(12))
        self.assertEqual(permutations, [
            ('a', 'b'), ('a', 'c'), ('a', 'd'), \
            ('b', 'a'), ('b', 'c'), ('b', 'd'), \
            ('c', 'a'), ('c', 'b'), ('c', 'd'), \
            ('d', 'a'), ('d', 'b'), ('d', 'c')
        ])
    
    def test_combinations(self):
        combo = self.itertools.combinations('12345', 3)
        combinations = list(next(combo) for _ in range(6))
        self.assertEqual(combinations, [
            ('1', '2', '3'), ('1', '2', '4'), ('1', '2', '5'), \
            ('1', '3', '4'), ('1', '3', '5'), ('1', '4', '5')
        ])

if __name__ == '__main__':
    unittest.main()
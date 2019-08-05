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
        self.assertListEqual(odds, [1,3,5,7,9])
    
    def test_cycle(self):
        cycler = self.itertools.cycle('abcd')
        cycle = list(next(cycler) for _ in range(8))
        self.assertListEqual(cycle, [
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
        self.assertListEqual(repeat, [
            'a', 'a', 'a', 'a', 'a', \
            'a', 'a', 'a', 'a', 'a'
        ])

    def test_product(self):
        productor = self.itertools.product(
            ['a', 'b','c'], \
            ['x', 'y', 'z']
        )
        cartesian_product = list(next(productor) for _ in range(9))
        self.assertListEqual(cartesian_product, [
            ('a', 'x'), ('a', 'y'), ('a', 'z'), \
            ('b', 'x'), ('b', 'y'), ('b', 'z'), \
            ('c', 'x'), ('c', 'y'), ('c', 'z')
        ])

    def test_self_product(self):
        prouctor = self.itertools.product([1, 2, 3], repeat=3)
        cartesian_product = list(next(prouctor) for _ in range(6))
        self.assertListEqual(cartesian_product, [
            (1,1,1), (1,1,2), (1,1,3), \
            (1,2,1), (1,2,2), (1,2,3)
        ])

    def test_full_permutations(self):
        permut = self.itertools.permutations('abc')
        permutaitons = list(next(permut) for _ in range(6))
        self.assertListEqual(permutaitons, [
            ('a', 'b', 'c'), ('a', 'c', 'b'), \
            ('b', 'a', 'c'), ('b', 'c', 'a'), \
            ('c', 'a', 'b'), ('c', 'b', 'a')
        ])

    def test_reduced_permutations(self):
        permut = self.itertools.permutations('abcd', 2)
        permutations = list(next(permut) for _ in range(12))
        self.assertListEqual(permutations, [
            ('a', 'b'), ('a', 'c'), ('a', 'd'), \
            ('b', 'a'), ('b', 'c'), ('b', 'd'), \
            ('c', 'a'), ('c', 'b'), ('c', 'd'), \
            ('d', 'a'), ('d', 'b'), ('d', 'c')
        ])
    
    def test_combinations(self):
        combo = self.itertools.combinations('12345', 3)
        combinations = list(next(combo) for _ in range(6))
        self.assertListEqual(combinations, [
            ('1', '2', '3'), ('1', '2', '4'), ('1', '2', '5'), \
            ('1', '3', '4'), ('1', '3', '5'), ('1', '4', '5')
        ])

    def test_combinations_with_replacement(self):
        combo = self.itertools.combinations_with_replacement('12345', 3)
        combinations = list(next(combo) for _ in range(6))
        self.assertListEqual(combinations, [
            ('1', '1', '1'), ('1', '1', '2'), ('1', '1', '3'), \
            ('1', '1', '4'), ('1', '1', '5'), ('1', '2', '2')
        ])
    
    def test_default_accumulate(self):
        first_five = [1, 2, 3, 4, 5]
        acc = self.itertools.accumulate(first_five)
        accumulations = list(next(acc) for _ in range(len(first_five)))
        self.assertListEqual(accumulations, [1, 3, 6, 10, 15])
    
    def test_accumulate_with_function(self):
        rand_nums = [7, 19, 33, 12]
        iter_function = lambda x, y: (x+y)*(x/y)
        acc = self.itertools.accumulate(rand_nums, iter_function)
        accumulations = list(round(next(acc), 2) for _ in range(len(rand_nums)))
        self.assertListEqual(accumulations, [7, 9.58, 12.36, 25.09])


if __name__ == '__main__':
    unittest.main()
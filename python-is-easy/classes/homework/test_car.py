from car import Car
import unittest

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(
            'Nissan',
            '370Z',
            2019,
            2)
    
    def test_drive(self):
        self.car.drive()
        self.assertTrue(self.car.isDriving)
    
    def test_stop(self):
        self.car.drive()
        self.car.stop()
        self.assertFalse(self.car.isDriving)
        self.assertEqual(self.car.trips_since_maintenance, 1)
    
    def test_needs_repair(self):
        for _ in range(101):
            self.car.drive()
            self.car.stop()
        self.assertGreater(self.car.trips_since_maintenance, 100)
        self.assertTrue(self.car.needs_maintenance)
    
if __name__ == '__main__':
    unittest.main()
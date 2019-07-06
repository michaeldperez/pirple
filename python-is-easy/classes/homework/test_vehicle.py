import unittest
from vehicle import Vehicle

class TestVehice(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(
            "Toyota",
            "4Runner",
            2016,
            3)

    def test_set_make(self):
        self.vehicle.set_make('Honda')
        self.assertEqual(self.vehicle.make, 'Honda')

    def test_set_model(self):
        self.vehicle.set_model('Accord')
        self.assertEqual(self.vehicle.model, 'Accord')
    
    def test_set_year(self):
        self.vehicle.set_year(2019)
        self.assertEqual(self.vehicle.year, 2019)
    
    def test_set_weight(self):
        self.vehicle.set_weight(2)
        self.assertEqual(self.vehicle.weight, 2)
    
    def test_repair(self):
        self.vehicle.trips_since_maintenance = 101
        self.vehicle.needs_maintenance = True
        self.vehicle.repair()
        self.assertFalse(self.vehicle.needs_maintenance)
        self.assertEqual(self.vehicle.trips_since_maintenance, 0)

if __name__ == '__main__':
    unittest.main()
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from eps_script import available_power, battery_charging

class TestEPS(unittest.TestCase):

    def test_available_power(self):
        """
        Tests the available_power function.
        """
        # Test case 1: Normal operation
        self.assertAlmostEqual(available_power(25, 10), 250, places=2)
        
        # Test case 2: Voltage over limit (should be clamped to 28V)
        # Power = 28V * 8A = 224W
        self.assertAlmostEqual(available_power(30, 8), 224, places=2)
        
        # Test case 3: Current over limit (should be clamped to 10A)
        # Power = 15V * 10A = 150W
        self.assertAlmostEqual(available_power(15, 12), 150, places=2)

    def test_battery_charging(self):
        """
        Tests the battery_charging function.
        """
        # E = P * t
        # E = 250W * 3600s = 900000 J
        self.assertAlmostEqual(battery_charging(250, 3600), 900000, places=2)

if __name__ == '__main__':
    unittest.main()

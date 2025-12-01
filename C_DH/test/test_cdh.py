import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cdh_script import parse_command

class TestCDH(unittest.TestCase):

    def test_parse_command_valid(self):
        """
        Tests the parse_command function with valid inputs.
        """
        cmd = "EPS:CMD01:0"
        expected = ("Electrical Power Subsystem", "BATTERY_CHARGE_MODE", 0)
        self.assertEqual(parse_command(cmd), expected)

        cmd = "TCS:CMD04:30"
        expected = ("Thermal Control Subsystem", "TEMP_SETPOINT", 30)
        self.assertEqual(parse_command(cmd), expected)

    def test_parse_command_invalid(self):
        """
        Tests the parse_command function with invalid inputs.
        The function should handle these gracefully, e.g., by returning (None, None, None).
        """
        # Invalid subsystem
        cmd = "XXX:CMD01:0"
        self.assertEqual(parse_command(cmd), (None, None, None))

        # Invalid command
        cmd = "RCS:INVALID:0"
        self.assertEqual(parse_command(cmd), (None, None, None))

        # Non-numeric parameter
        cmd = "EPS:CMD01:ABC"
        self.assertEqual(parse_command(cmd), (None, None, None))
        
        # Incorrect format
        cmd = "EPS-CMD01-0"
        self.assertEqual(parse_command(cmd), (None, None, None))

if __name__ == '__main__':
    unittest.main()

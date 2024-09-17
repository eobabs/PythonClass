import unittest
import powerfour


class TestPowerFour(unittest.TestCase):
	def test_that_powerfour_function_exist(self):
		powerfour.get_power(3)
	
	def test_that_powerfour_function_returns_powerfour_result(self):
		self.assertEqual(powerfour.get_power(3), 81)
	
	def test_that_powerfour_function_raise_error_with_negative_amount(self):
		self.assertRaises(ValueError,powerfour.get_power, -16)
	
	def test_that_powerfour_function_raise_error_with_string_input(self):
		self.assertRaises(TypeError,powerfour.get_power, "abc")
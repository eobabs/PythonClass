import unittest
import dollartonaira


class TestDollarToNaira(unittest.TestCase):

	def test_dollartonaira_get_naira_function_exists(self):
		self.assertTrue(callable(dollartonaira.get_naira), "function doesnot exist")

	def test_dollartonaira_get_naira_function_returns_valid_conversion(self):
		self.assertEqual(dollartonaira.get_naira(1),1550)

	def test_dollartonaira_get_naira_function_returns_valid_conversion_with_floating_values(self):		self.assertEqual(dollartonaira.get_naira(0.5),775.0)

	def test_invalid_input(self):
		self.assertEqual(dollartonaira.get_naira("abc"), "Invalid input. Enter a valid number")
		self.assertEqual(dollartonaira.get_naira(None), "Invalid input. Enter a valid number")

	def test_dollartonaira_get_naira_function_raise_error_with_negative_amount(self):
		with self.assertRaises(ValueError):
			dollartonaira.get_naira (-16)
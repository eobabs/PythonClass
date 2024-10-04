import unittest
import divideorsquare


class TestDivideOrSquare(unittest.TestCase):

	def test_divideorsquare_divide_or_square_function_exists(self):
		self.assertTrue(callable(divideorsquare.divide_or_square), "function doesnot exist")

	def test_divideorsquare_divide_or_square_function_returns_square_root_or_remainder(self):
		self.assertEqual(divideorsquare.divide_or_square(10),3,16)

	def test_divideorsquare_divide_or_square_function_returns_square_root(self):		self.assertEqual(divideorsquare.divide_or_square(456.3),21.36)

	def test_invalid_inputdivide_or_square_function_returns_error_with_non_numbers(self):
		self.assertEqual(TypeError,divideorsquare.divide_or_square("abc"), "Invalid input. Enter a valid number")
		self.assertEqual(TypeError,divideorsquare.divide_or_square(None), "Invalid input. Enter a valid number")

	def test_divideorsquare_divide_or_square_function_raise_error_with_negative_numbers(self):
		self.assertRaises(ValueError, divideorsquare.divide_or_square (-16),"Invalid. Enter a positive number"):
		self.assertRaises(ValueError, divideorsquare.divide_or_square (-12.5),"Invalid. Enter a positive number"):
			
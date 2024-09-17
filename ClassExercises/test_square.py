import unittest
import square


class TestSquare(unittest.TestCase):
	def test_that_square_function_exist(self):
		square.get_square(3)
	
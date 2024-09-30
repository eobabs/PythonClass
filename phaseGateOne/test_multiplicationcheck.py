import unittest
import multiply from 



class TestMultiplyFunction(unittest.TestCase):
    
    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_multiply_one(self):
        self.assertEqual(multiply(1, 5), 5)
        self.assertEqual(multiply(5, 1), 5)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply(1000, 2000), 2000000)
        self.assertEqual(multiply(-1000, 2000), -2000000)



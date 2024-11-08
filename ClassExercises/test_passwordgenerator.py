import unittest
import string
from passwordgenerator import generate_password

class TestPasswordGenerator(unittest.TestCase):

	def test_that_generate_password_functionexist(self):
		generate_password()

	def test_password_length(self):
        	self.assertGreaterEqual(len(generate_password()), 17)
        	self.assertLessEqual(len(generate_password()), 50)

	def test_that_password_has_numbers(self):
		 self.assertFalse(generate_password().isdigit())

	def test_that_password_has_alphabets(self):
		 self.assertFalse(generate_password().isalpha())

	def test_that_password_has_punctuation(self):
		 self.assertFalse(generate_password().isalpha())

	
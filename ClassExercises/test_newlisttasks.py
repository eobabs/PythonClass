import unittest
from newlisttasks import add_third_number
from newlisttasks import add_border_number





class NewListTasks(unittest.TestCase):
    def test_that_function_add_every_third_element_exists(self):
        numbers = [1, 7, 8, 9, 10, 34]
        add_third_number(numbers)

    def test_that_function_adds_every_third_element(self):
        numbers = [1, 2, 3, -4, 5, -6]

        result = -3
        self.assertEqual(add_third_number(numbers), result)

    def test_that_function_adds_first_last_and_middle_element(self):
        numbers = [1, 2, 3, 4, 5, 6]
        lists = [1, 5, 7, 8, 9]
        self.assertEqual(add_border_number(numbers), 10.5)
        self.assertEqual(add_border_number(lists), 17)

    def test_that_function_add_every_third_element_throws_error_with_string_value(self):
        self.assertRaises(TypeError, add_third_number, [1, 3, 4, 5, 9,'a', 3])


if __name__ == '__main__':
    unittest.main()

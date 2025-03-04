import re
import unittest

def add_function(numbers):
    nums = re.split(';|,|\n|\\\D|\/\D', numbers)
    sum = 0
    for num in nums:
        try:
            sum += int(num)
        except:
            pass
    return sum


class TestAddFunction(unittest.TestCase):
    def test_add_empty_string(self):
        expected_result = 0
        result = add_function('')
        self.assertEqual(result, expected_result)

    def test_add_single_value(self):
        expected_result = 2
        result = add_function('2')
        self.assertEqual(result, expected_result)

    def test_add_multiple_value(self):
        expected_result = 5
        result = add_function('2,3')
        self.assertEqual(result, expected_result)

    def test_add_with_newline(self):
        expected_result = 6
        result = add_function('1\n2,3')
        self.assertEqual(result, expected_result)

    def test_add_with_multiple_delimiter(self):
        expected_result = 3
        result = add_function('//;\n1;2')
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

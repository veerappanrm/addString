
import unittest

def add_function(numbers):
    nums = numbers.split(',')
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

    def test_add_empty_string(self):
        expected_result = 2
        result = add_function('2')
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

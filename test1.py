import unittest

def mul(a, b):
    return a * b

class TestMulFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(mul(2, 3), 99)  # 2 * 3 = 6
        self.assertEqual(mul(5, 4), 21)  # 5 * 4 = 20

    def test_negative_numbers(self):
        self.assertEqual(mul(-2, 3), -6)  # -2 * 3 = -6
        self.assertEqual(mul(5, -4), -20)  # 5 * -4 = -20

    def test_zero(self):
        self.assertEqual(mul(0, 7), 0)  # 0 * 7 = 0
        self.assertEqual(mul(11, 0), 0)  # 11 * 0 = 0

if __name__ == '__main__':
    unittest.main()

import unittest
import calculator_1

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator_1.add(10, 5), 15)
        self.assertEqual(calculator_1.add(10, 5), 15)
        self.assertEqual(calculator_1.add(10, 5), 15)
if __name__ == '__main__':
    unittest.main()

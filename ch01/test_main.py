import unittest
import main

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = main.calculate_sum(1, 1)
        self.assertEqual(result, 2)

    def test_sub(self):
        result = main.calculate_sub(1, 1)
        self.assertEqual(result, 0)

    def test_div(self):
        self.assertEqual(main.calculate_div(10, 2), 5)

        with self.assertRaises(ValueError):
            main.calculate_div(10, 0)

if __name__ == "__main__":
    unittest.main()
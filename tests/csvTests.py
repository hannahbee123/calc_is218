import unittest
from src.csv.csvReader import CsvReader, ClassFactory
from src.calculator.calculator import Calculator
# from pprint import pprint


class CSVTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        test_data = CsvReader('/data/addition.csv').data
        for row in test_data:
            self.assertEqual(calculator.add(float(row['Value 1']), float(row['Value 2'])), float(row['Result']))
            self.assertEqual(calculator.result, float(row['Result']))


'''
    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.result, 0)

    def test_multiply_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_divide_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(2, 2), 1)
        self.assertEqual(calculator.result, 1)

    def test_square_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(2), 4)
        self.assertEqual(calculator.result, 4)

    def test_square_root_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square_root(4), 2)
        self.assertEqual(calculator.result, 2)
'''

if __name__ == '__main__':
    unittest.main()

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
        test_data.clear()

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        test_data = CsvReader('/data/subtraction.csv').data
        for row in test_data:
            self.assertEqual(calculator.subtract(float(row['Value 2']), float(row['Value 1'])), float(row['Result']))
            self.assertEqual(calculator.result, float(row['Result']))
        test_data.clear()

    def test_multiply_method_calculator(self):
        calculator = Calculator()
        test_data = CsvReader('/data/multiplication.csv').data
        for row in test_data:
            self.assertEqual(calculator.multiply(float(row['Value 1']), float(row['Value 2'])), float(row['Result']))
            self.assertEqual(calculator.result, float(row['Result']))
        test_data.clear()

    def test_divide_method_calculator(self):
        calculator = Calculator()
        test_data = CsvReader('/data/division.csv').data
        for row in test_data:
            self.assertEqual(calculator.divide(float(row['Value 2']), float(row['Value 1'])), (float(row['Result'])))
            self.assertEqual(calculator.result, (float(row['Result'])))
        test_data.clear()

    def test_square_method_calculator(self):
        calculator = Calculator()
        test_data = CsvReader('/data/square.csv').data
        for row in test_data:
            self.assertEqual(calculator.square(float(row['Value 1'])), float(row['Result']))
            self.assertEqual(calculator.result, float(row['Result']))
        test_data.clear()

    def test_square_root_method_calculator(self):
        calculator = Calculator()
        test_data = CsvReader('/data/squareRoot.csv').data
        for row in test_data:
            self.assertEqual(calculator.square_root(float(row['Value 1'])), round(float(row['Result']), 8))
            self.assertEqual(calculator.result, round(float(row['Result']), 8))
        test_data.clear()


if __name__ == '__main__':
    unittest.main()

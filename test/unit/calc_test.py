import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_potentiation_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.potentiation(2, 2))
        self.assertEqual(9, self.calc.potentiation(3, 2))
        self.assertEqual(16, self.calc.potentiation(4, 2))
        self.assertEqual(8, self.calc.potentiation(2, 3))
    
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(3, self.calc.sqrt(9))
        self.assertEqual(4, self.calc.sqrt(16))
        self.assertEqual(5, self.calc.sqrt(25))
        self.assertEqual(2, self.calc.sqrt(4))
    
    def test_sqrt_method_fails_with_sqrt_by_negative(self):
        self.assertRaises(TypeError, self.calc.sqrt, -2)
        self.assertRaises(TypeError, self.calc.sqrt, -22)


    def test_logarithm_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.logarithm(10))
        self.assertEqual(1.40, self.calc.logarithm(25))
        self.assertEqual(1.56, self.calc.logarithm(36))
        self.assertEqual(1.26, self.calc.logarithm(18))

    def test_logarithm_method_fails_with_logarithm_by_zero(self):
        self.assertRaises(TypeError, self.calc.logarithm,  0)
   
    
    


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

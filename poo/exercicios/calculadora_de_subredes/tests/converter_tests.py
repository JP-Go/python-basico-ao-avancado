import unittest
from ...calculadora_de_subredes import converter


class NumberConverterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.converter = converter.NumberConverter()

    def tearDown(self) -> None:
        del self.converter

    def test_convert_to_byte(self):
        self.assertEqual(self.converter.convert_int_to_byte(0), "00000000")
        self.assertEqual(self.converter.convert_int_to_byte(1), "00000001")
        self.assertEqual(self.converter.convert_int_to_byte(255), "11111111")

    def test_convert_to_byte_edge_cases(self):
        self.assertRaises(ValueError, self.converter.convert_int_to_byte, -1)
        self.assertRaises(ValueError, self.converter.convert_int_to_byte, "hi")

    def test_convert_to_int(self):
        self.assertEqual(self.converter.convert_byte_to_int("1"), 1)
        self.assertEqual(self.converter.convert_byte_to_int("10"), 2)
        self.assertEqual(self.converter.convert_byte_to_int("10"), 2)

    def test_convert_to_int_edge_cases(self):
        self.assertRaises(ValueError, self.converter.convert_byte_to_int, -1)
        self.assertRaises(ValueError, self.converter.convert_byte_to_int, "hi")

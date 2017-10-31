import unittest
from foobarqix import foobarqix


class FoobarQixTestCase(unittest.TestCase):
    def test_retrurn_Foo_when_number_is_divisible_by_3(self):
        self.assertEqual(foobarqix(3), "Foo")
        self.assertEqual(foobarqix(6), "Foo")
        self.assertEqual(foobarqix(9), "Foo")

    def test_retrurn_Bar_when_number_is_divisible_by_5(self):
        self.assertEqual(foobarqix(5), "Bar")

    def test_retrurn_Qix_when_number_is_divisible_by_7(self):
        self.assertEqual(foobarqix(7), "Qix")

    def test_retrurn_FooBar_when_number_is_divisible_by_3_and_5(self):
        self.assertEqual(foobarqix(15), "FooBar")

    def test_return_number_as_a_string_otherwise(self):
        self.assertEqual(foobarqix(1),"1")
        self.assertEqual(foobarqix(2),"2")


unittest.main()

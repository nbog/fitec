import unittest


def is_divisible(number, divisor):
    return number % divisor == 0


def foobarqix(number):
    if is_divisible(number, 3):
        return "Foo"
    if is_divisible(number, 5):
        return "Bar"
    if is_divisible(number, 7):
        return "Qix"

class FoobarQixTestCase(unittest.TestCase):
    def test_retrurn_Foo_when_number_is_divisible_by_3(self):
        self.assertEqual(foobarqix(3), "Foo")

    def test_retrurn_Bar_when_number_is_divisible_by_5(self):
        self.assertEqual(foobarqix(5), "Bar")

    def test_retrurn_Qix_when_number_is_divisible_by_7(self):
        self.assertEqual(foobarqix(7), "Qix")


unittest.main()

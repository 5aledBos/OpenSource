from unittest import TestCase
from main_dir.app import is_odd, is_even, odd_even


class MyFunctionsTestCase(TestCase):
    def test_is_even(self):
        num = 1234
        self.assertTrue(is_even(num))
        with self.assertRaises(ValueError):
            is_even('NOT A NUMBER')

    def test_is_odd(self):
        num = 12345
        self.assertTrue(is_odd(num))
        with self.assertRaises(ValueError):
            is_odd('NOT A NUMBER')

    def test_type(self):
        self.assertEqual(odd_even(123), 'ODD')
        self.assertEqual(odd_even(122), 'EVEN')

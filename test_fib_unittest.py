import unittest
from multiprocessing.managers import Value

from fib import fibonacci_iterative

#para cuando tnegamos que hacaer <20 tests
class TestFib(unittest.TestCase):
    def test_fib_9_is_34(self):
        assert self.assertEqual(fibonacci_iterative(9),34)

    def test_fib_9_is_34(self):
        expected = 55
        result = fibonacci_iterative(9)
        self.assertEqual(expected,result)

    def test_split(self):
        with self.assertRaises(ValueError):
            fibonacci_iterative(-1)

if __name__ == '__main__':
    result = fibonacci_iterative(9)
    print(result)


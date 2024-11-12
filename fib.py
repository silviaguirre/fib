import argparse
from functools import cache

def fibonacci_iterative(n: int) -> int:
    """
    Computes the n-th Fibonacci number.
    :param n: n-th Fibonacci number.
    :return: The n-th Fobonacci number.
    """

    if n < 0:
        raise ValueError("n must be greater or equal to zero.")
    if n < 2:
        return n
    n0 = 0
    n1 = 1
    for _ in range(n):  # _ en vez de i xque no la usa para nada
        nth = n0 + n1
        n0 = n1
        n1 = nth

    return nth



@cache
def fibonacci_recursive(n: int) -> int:
    """
    Computes the n-th Fibonacci number using a recursive method.
    :param n: n-th Fibonacci number.
    :return: The i-th Fobonacci number.
    """
    if n < 0:
        raise ValueError("n must be greater or equal to zero.")
    if n < 2:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('nth', type=int, help="Nth Fibonacci number.")  # positional argument

    args = parser.parse_args()

    result = fibonacci_iterative(args.nth)
    print(result)

"""
An empty python package.

>>> from prototype_python_library import fib
>>> fib(0)
0
"""

__version__ = "0.4.0"


def fib(n: int):
    """Compute the nth element in the fibonacci sequence."""
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

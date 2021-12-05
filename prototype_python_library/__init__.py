"""
>>> from prototype_python_library import fib
>>> fib(0)
0
"""

__version__ = "0.3.0"


def fib(n: int):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

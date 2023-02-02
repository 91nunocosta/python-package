"""Test prototype_python_library module."""
from prototype_python_library import add, fib, multiply, subtract


def test_add():
    """Test add function."""
    assert add(0, 0) == 0
    assert add(1, 2) == 3


def test_subtract():
    """Test subtract function."""
    assert subtract(5, 3) == 2


def test_multiply():
    """Test multiply function."""
    assert multiply(2, 2) == 4


def test_fib():
    """Test fib function."""
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8

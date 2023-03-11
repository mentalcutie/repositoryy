import pytest
from main import multiply, summa


def test_multiply():
    assert multiply(2, 3) == 6


def test_multiply_zero():
    assert multiply(1, 0) == 0


def test_multiply_error():
    with pytest.raises(TypeError):
        multiply("a", "b")


def test_summa():
    assert summa(2, 2) == 4

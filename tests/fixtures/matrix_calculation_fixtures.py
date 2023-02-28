"""Necessary fixtures to test the string_manipulation.py package"""
import pytest


@pytest.fixture
def identity_matrix_3x3():
    """Returns a 3x3 identity matrix"""
    return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


@pytest.fixture
def ones_3x3():
    return [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

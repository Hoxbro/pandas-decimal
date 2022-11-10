import pytest

import numpy as np
import pandas as pd

@pytest.mark.parametrize("degree", [0,1,2,3])
def test_adding_of_same_degree_works_by_item(degree):
    dtype_str = f'decimal[{degree}]'
    original = [0,1,2,3]
    expected = [x+y for x,y in zip(original, original)]
    x = pd.Series(original, dtype=dtype_str)
    y = pd.Series(original, dtype=dtype_str)
    z = x + y
    # Test degree didn't change
    assert str(x.dtype) == dtype_str
    # Test values are correct
    assert all([i == j for i, j in zip(expected, z)])

@pytest.mark.parametrize("degree", [0,1,2,3])
def test_adding_of_same_degree_works_by_vector(degree):
    dtype_str = f'decimal[{degree}]'
    original = [0,1,2,3]
    expected = [x+y for x,y in zip(original, original)]
    x = pd.Series(original, dtype=dtype_str)
    y = pd.Series(original, dtype=dtype_str)
    z = x + y
    # Test degree didn't change
    assert str(x.dtype) == dtype_str
    # Test values are correct
    assert np.all(expected == z)
"""
@pytest.mark.parametrize("delta_degree", [1,2,3])
def test_adding_of_different_degree_works(delta_degree):
    degree = 0
    other_degree = degree + delta_degree
    dtype_str = f'decimal[{degree}]'
    original = [0,1,2,3]
    expected = [x+y for x,y in zip(original, original)]
    x = pd.Series(original, dtype=dtype_str)
    y = pd.Series(original, dtype=dtype_str)
    z = x + y
    # Test degree didn't change
    assert str(x.dtype) == dtype_str
    # Test values are correct
    assert all([np.isclose(x, y) for x, y in zip(expected, z)])

@pytest.mark.parametrize("delta_degree", [1,2,3])
def test_adding_of_different_degree_works2(delta_degree):
    degree = 0
    other_degree = degree + delta_degree
    dtype_str = f'decimal[{degree}]'
    original = [0,1,2,3]
    expected = [x+y for x,y in zip(original, original)]
    x = pd.Series(original, dtype=dtype_str)
    y = pd.Series(original, dtype=dtype_str)
    z = x + y
    # Test degree didn't change
    assert str(x.dtype) == dtype_str
    # Test values are correct
    assert np.all(expected == z)

"""
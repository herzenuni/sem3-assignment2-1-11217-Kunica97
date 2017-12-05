import pytest
import sort
import hypothesis.strategies as st
from hypothesis import given

@given(st.lists(st.integers()))
def test_bubble(arr):
    assert sort.bubble(arr) == sorted(arr)

@given(st.lists(st.integers()))
def test_qsort(arr):
    assert sort.quick(arr) == sorted(arr)
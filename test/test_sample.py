# tests/test_sample1.py
import pytest
import sys
import os

# Add the srs directory to sys.path so Python can find it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../srs')))

from sample1 import add, subtract  # Import functions from srs/sample1.py

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    assert subtract(-5, -5) == 0

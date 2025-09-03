# test_demo.py

import pytest
from app import calculate_area, calculate_perimeter

def test_calculate_area():
    assert calculate_area(0) == 0
    assert calculate_area(1) == 1
    assert calculate_area(2.5) == 6.25
    assert calculate_area(10) == 100

def test_calculate_perimeter():
    assert calculate_perimeter(0) == 0
    assert calculate_perimeter(1) == 4
    assert calculate_perimeter(2.5) == 10.0
    assert calculate_perimeter(10) == 40

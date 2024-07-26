import pytest 
from pytest import mark 


@mark.parametrize("num1, num2 ,expected", 
                  [(2, 5, 7), 
                   (3, 7, 10)])  
def test_addition(num1, num2, expected): 
    assert num1 + num2 == expected 
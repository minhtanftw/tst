import pytest 
from app import add,divide

def test_add():
    assert add(3,2) == 5
def test_divide():
    assert divide(10,2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
import pytest
from .miniMaxSum import miniMaxSum

    
def test_happy_sample(capfd):
    miniMaxSum([1,2,3,4,5])
    out, err = capfd.readouterr()
    assert out == "10 14\n"
    assert err == ''
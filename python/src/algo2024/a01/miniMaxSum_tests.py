import pytest
from .miniMaxSum import miniMaxSum, miniMaxSum_manual

    
def test_happy_sample(capfd):
    miniMaxSum([1,2,3,4,5])
    out, err = capfd.readouterr()
    assert out == "10 14\n"
    assert err == ''


def test_happy_sample_manual(capfd):
    miniMaxSum_manual([1,2,3,4,5])
    out, err = capfd.readouterr()
    assert out == "10 14\n"
    assert err == ''
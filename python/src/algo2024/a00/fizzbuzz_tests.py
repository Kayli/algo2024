import pytest
from .fizzbuzz import fizzbuzz, _fizzbuzz_arr, _fizzbuzz_single


def test_happy_sample(capfd):
    fizzbuzz(5)
    out, err = capfd.readouterr()
    assert out == "1\n2\nfizz\n4\nbuzz\n"
    assert err == ''


def test_fizzbuzz_arr_returns_array_of_proper_len():
    assert len(_fizzbuzz_arr(1)) == 1
    assert len(_fizzbuzz_arr(5)) == 5


@pytest.mark.parametrize("test_input,expected", [
    (3, 'fizz'),
    (5, 'buzz'),
    (15, 'fizzbuzz'),
    (2, 2),
    (22, 22)
])
def test_single_happy_samples(test_input, expected):
    assert _fizzbuzz_single(test_input) == expected


def test_argument_of_invalid_type():
    with pytest.raises(TypeError):
        _fizzbuzz_single('invalid')

def test_out_of_range_argument():
    with pytest.raises(ValueError):
        fizzbuzz(0)
    
    with pytest.raises(ValueError):
        fizzbuzz(-5)

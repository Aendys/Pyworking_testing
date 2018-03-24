from fb import fizzbuzz
import pytest

def test_fizzbuzz_returns_string():
	assert isinstance(fizzbuzz(1), str) 

@pytest.mark.parametrize('num', [1,2,4,7,8,11,13,14])
def test_fizzbuzz_regular_returs_self(num):
	assert fizzbuzz(num) == str (num)	

@pytest.mark.parametrize('num', [3,6,9,12])
def test_fizzbuzz_3div_returns_fizz(num):
        assert fizzbuzz(num) ==  'fizz'

@pytest.mark.parametrize('num', [5,10])
def test_fizzbuzz_5div_returs_buzz(num):
        assert fizzbuzz(num) == 'buzz'

@pytest.mark.parametrize('num', [15])
def test_fizzbuzz_3div_5div_returs_fizzbuzz(num):
        assert fizzbuzz(num) == 'fizzbuzz'

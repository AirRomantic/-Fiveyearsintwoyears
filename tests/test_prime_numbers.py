from main import prime_numbers
import pytest


@pytest.mark.parametrize('low, high, result', [(5, 14, [5, 7, 11, 13]),
                                               ('sdfsd', 10, []),
                                               (5, 'asdasd', [])])
def test_prime_numbers(low, high, result):
    assert prime_numbers(low, high) == result


from main import roman_numerals_to_int
import pytest


@pytest.mark.parametrize('roman_numeral, result', [('VIX', 14),
                                                   ('MMXI', 2011),
                                                   ('MMMCMXCIX', 3999),
                                                   ('',0)])
def test_roman_numerals_to_int(roman_numeral, result):
    assert roman_numerals_to_int(roman_numeral) == result


@pytest.mark.parametrize('roman_numeral, exeption', [('MMYI', KeyError),
                                                     (234,TypeError)])
def test_roman_numerals_to_int_eror(roman_numeral, exeption):
    with pytest.raises(exeption):
        roman_numerals_to_int(roman_numeral)



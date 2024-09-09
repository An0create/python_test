import pytest
import spellcheck


# alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"


@pytest.fixture
def input_value():
    input = beta
    return input


def test_length(input_value):
    assert spellcheck.word_count(input_value) < 10
    assert spellcheck.char.count(input_value) < 50



def test_struc(input_value):
    assert spellcheck.first_char(input_value).isupper()
    assert spellcheck.last_char(input_value) == '.'


# Run these tests with `python3 -m pytest test_spellcheck.py`
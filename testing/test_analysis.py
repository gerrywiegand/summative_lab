import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

import pythonAssessment as pa
import utils


def test_validate_input():
    with pytest.raises(TypeError):
        utils.validate_input(123)
    with pytest.raises(ValueError):
        utils.validate_input("   ")
    # Valid input should not raise an error
    utils.validate_input("Valid string")


def test_tokenize_text():
    text = "Hello, World! This is a test."
    tokens = utils.tokenize_text(text)
    assert tokens == ["hello", "world", "this", "is", "a", "test"]


def test_count_specific_word():
    assert pa.count_specific_word("text", pa.sample_text) == 2
    assert pa.count_specific_word("sample", pa.sample_text) == 1
    assert pa.count_specific_word("missing", pa.sample_text) == 0


def test_identify_most_common_word():
    assert pa.identify_most_common_word(pa.sample_text) == "is"


def test_calculate_average_word_length():
    assert pa.calculate_average_word_length(pa.sample_text) == 5.0


def test_count_paragraphs():
    assert pa.count_paragraphs(pa.sample_text) == 2


def test_count_sentences():
    assert pa.count_sentences(pa.sample_text) == 3

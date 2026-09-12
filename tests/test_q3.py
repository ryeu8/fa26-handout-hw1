"""HW1 Question 3 Tests"""

import sys

sys.path.append('.')
from src.q3 import capitalize_words

def test_capitalize_words_no_change() -> None:
    """Test that a string that does not need to be changed remains unchanged."""
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_words_single_word() -> None:
    """Test that a single word is capitalized."""
    assert capitalize_words("hello") == "Hello"

def test_capitalize_words_ending_character() -> None:
    """Test that a string ending with a special character is capitalized."""
    assert capitalize_words("hello world!") == "Hello World!"

def test_capitalize_words_second_word() -> None:
    """Test that a string with two words capitalizes 
    the second word if the first in capitalized already"""
    assert capitalize_words("Hello world") == "Hello World"

def test_capitalize_words_special_characters_starts() -> None:
    """Test that a string with special characters at the start of 
    words capitalizes the first letter after the special character."""
    assert capitalize_words("??hello ?world") == "??Hello ?World"

def test_capitalize_words_empty() -> None:
    """Test that an empty string returns an empty string."""
    assert capitalize_words("") == ""

def test_capitalize_words_numbers() -> None:
    """Test that a string with only numbers and special characters remains unchanged."""
    assert capitalize_words("1234567890!@#$%^&*()") == "1234567890!@#$%^&*()"

def test_capitalize_words_starting_space() -> None:
    """Test that a string with a starting space remains unchanged."""
    assert capitalize_words("  hello world") == "  Hello World"

def test_capitalize_words_triple_space() -> None:
    """Test that a string with three spaces is capitalized correctly."""
    assert capitalize_words("hello   world") == "Hello   World"

def test_capitalize_words_starting_number() -> None:
    """Test that a string with starting numbers capitalizes 
    the first letter after the number."""
    assert capitalize_words("123hello 456world") == "123Hello 456World"

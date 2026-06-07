import pytest
from lib.palindrome import longest_palindromic_substring


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("cbbd", "bb"),
        ("a", "a"),
        ("racecar", "racecar"),
        ("aaaa", "aaaa"),
    ]
)
def test_known_palindromes(input_str, expected):
    assert longest_palindromic_substring(input_str) == expected


def test_babad_returns_valid_answer():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]


def test_two_different_characters():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_no_long_palindrome():
    result = longest_palindromic_substring("abcdef")
    assert result in list("abcdef")
    assert len(result) == 1


def test_even_length_palindrome():
    assert longest_palindromic_substring("abccba") == "abccba"
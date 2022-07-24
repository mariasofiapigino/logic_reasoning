"""Logic reasoning tests"""
import pytest

from logic_reasoning.balanced_parentheses import count_balanced_parentheses
from logic_reasoning.find_and_multiply import find_and_multiply


@pytest.mark.parametrize(
    "test_phrase, expected",
    [
        ("((()()))", True),
        ("((()", False),
        ("(())", True),
        (")(", False),
        ("(()", False),
        ("(()()())", True),
        ("(text)(text)", True),
        ("()()(", False)
    ],
)
def test_balanced_parentheses(test_phrase: str, expected: bool) -> None:
    """Test different use cases for the function count_balanced_parentheses."""
    assert count_balanced_parentheses(test_phrase) == expected


@pytest.mark.parametrize(
    "numbers, search_value, expected",
    [
        ([1, 5, 1010, 1012], 2022, 1022120),
        ([1, 5, 1010, 1013], 2022, False),
        ([1, 5, 1010, 2021], 2022, 2021),
        ([1, -5, 2027, 2022], 2022, -10135),
        ([1, -5, 2027, 2021], 2022, 2021),  # If there are more than one pair of numbers, it keeps the first one.
    ],
)
def test_find_and_multiply(numbers: list, search_value: int, expected: int) -> None:
    """Test different successful use cases for the function find_and_multiply."""
    assert find_and_multiply(numbers, search_value) == expected


@pytest.mark.parametrize(
    "numbers, search_value, error_message",
    [
        ([1, 5, 1010, 1012], "2022", "The value of 'search_value' must be an integer."),
        ([1, 5, "1010", 1013], 2022, "The list of numbers to evaluate must all have integer values."),
    ],
)
def test_find_and_multiply_fails(numbers: list, search_value: int, error_message: int) -> None:
    """Test different failure use cases for the function find_and_multiply."""
    with pytest.raises(ValueError) as value_error:
        find_and_multiply(numbers, search_value)
    assert value_error.value.args[0] == error_message

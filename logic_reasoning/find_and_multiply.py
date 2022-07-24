from typing import Union, List


def find_and_multiply(numbers: List[int], search_value: int) -> Union[int, bool]:
    """Find the first two numbers that add up to the value of 'search_value',
    and return the multiplication of them.
    Args:
        numbers(List[int]): List of integers to analyze if the searched pair exists.
        search_value(int): Value to search for.
    Return:
        The multiplication of the numbers, if at least one pair of numbers was found in the list
        that added together give the desired value and false otherwise.
    Raises:
        ValueError: If the numbers are not integers."""
    if not isinstance(search_value, int):
        raise ValueError("The value of 'search_value' must be an integer.")

    for index, number in enumerate(numbers):
        if not isinstance(number, int):
            raise ValueError("The list of numbers to evaluate must all have integer values.")

        complementary = search_value - number
        if complementary in numbers[index + 1:]:
            return number * complementary
    return False

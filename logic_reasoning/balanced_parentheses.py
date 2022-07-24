def count_balanced_parentheses(phrase: str) -> bool:
    """Count that the parentheses of a sentence are balanced.
    That is, that there are the same number of characters of '(' as of ')' and that they start with '('
    Args:
        phrase(str): Phrase that you want to know if it has balanced parentheses.
    Return:
        bool: True if the parentheses are balanced in the sentence and false otherwise."""
    first_open_parenthesis_index = phrase.index("(")
    first_close_parenthesis_index = phrase.index(")")

    if first_open_parenthesis_index > first_close_parenthesis_index:
        return False

    num_open_parentheses = phrase.count("(")
    num_close_parentheses = phrase.count(")")

    return num_open_parentheses == num_close_parentheses

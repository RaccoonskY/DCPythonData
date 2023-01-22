"""
Example of using Doc Testing method
"""

def is_braces_sequence_correct(seq: str) -> bool:
    """
    Check correctness of braces sequence in statement
    >>> is_braces_sequence_correct("()(())")
    True
    >>> is_braces_sequence_correct("()[()]")
    True
    >>> is_braces_sequence_correct(")")
    False
    >>> is_braces_sequence_correct("[()")
    False
    >>> is_braces_sequence_correct("[(])")
    False
    """
    stack = []
    correspondent = dict(zip("([{", ")]}"))
    for brace in seq:
        if brace in "([{":
            stack.append(brace)
            continue
        elif brace in ")]}":
            if len(stack) == 0:
                return False
            left = stack.pop()
            if correspondent[left] != brace:
                return False
    return stack.__len__() == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()

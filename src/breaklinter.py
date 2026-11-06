# Pylint C0301 (line-too-long): this comment intentionally exceeds the 80-character configured limit.


def nested_blocks(first, second, third):
    # Pylint R1702 (too-many-nested-blocks): configured maximum is 2.
    if first:
        if second:
            if third:
                return True
    return False


def many_branches(value):
    # Pylint R0912 (too-many-branches) and R0915 (too-many-statements).
    result = "other"
    if value == 0:
        result = "zero"
    elif value == 1:
        result = "one"
    elif value == 2:
        result = "two"
    elif value == 3:
        result = "three"
    elif value == 4:
        result = "four"
    elif value == 5:
        result = "five"
    elif value == 6:
        result = "six"
    elif value == 7:
        result = "seven"
    elif value == 8:
        result = "eight"
    return result

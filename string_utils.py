def split_before_each_uppercases(input):
    """
    Splits a string before every uppercase character.
    Uppercase letters remain in the resulting parts.
    """
    if not input:
        return []

    parts = []
    current = input[0]

    for ch in input[1:]:
        if ch.isupper():
            parts.append(current)
            current = ch
        else:
            current += ch

    parts.append(current)
    return parts

def split_at_first_digit(s):
    """
    Splits a string into:
      1) prefix before the first digit
      2) integer starting from the first digit

    If no digit exists:
        return (original_string, 1)
    """
    for i, ch in enumerate(s):
        if ch.isdigit():
            # First digit found
            prefix = s[:i]
            number = int(s[i:])
            return prefix, number

    # No digit found
    return s, 1

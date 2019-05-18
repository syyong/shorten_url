"""
Utilities for encoding / decoding an integer into a base encoded value
Original source: https://stackoverflow.com/a/1052896
"""
# pylint: disable=invalid-name
import string

# generate a random bit order
# you'll need to save this mapping permanently, perhaps just hardcode it
# map how ever many bits you need to represent your integer space
mapping = list(range(28))
mapping.reverse()


# letters and digits for changing from base 10
chars = string.ascii_letters + string.digits


def encode(n):
    """shuffle the bits"""
    result = 0
    for i, b in enumerate(mapping):
        b1 = 1 << i
        b2 = 1 << b
        if n & b1:
            result |= b2
    return result


def decode(n):
    """unshuffle the bits"""
    result = 0
    for i, b in enumerate(mapping):
        b1 = 1 << i
        b2 = 1 << b
        if n & b2:
            result |= b1
    return result


def enbase(x):
    """change the base"""
    n = len(chars)
    if x < n:
        return chars[x]
    return enbase(int(x / n)) + chars[x % n]


def debase(x):
    """go back to base 10"""
    n = len(chars)
    result = 0
    for i, c in enumerate(reversed(x)):
        result += chars.index(c) * (n ** i)
    return result


def encode_and_enbase(n):
    """simplify the encode -> enbase process"""
    return enbase(encode(n))


def debase_and_decode(code):
    """simplify the debase -> decode process"""
    return decode(debase(code))

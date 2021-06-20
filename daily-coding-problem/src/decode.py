from string import ascii_lowercase as a2z
def decode(encoded: str) -> int:
    mapping = {k: v + 1 for v, k in enumerate(a2z)}

    no_two_tuples = 0
    decoadable = 1
    for i, s in enumerate(encoded):
        if i < len(encoded) - 1:
            if int(s + encoded[i + 1]) < 27:
                no_two_tuples += 1

    return decoadable + no_two_tuples




assert decode('111') == 3
assert decode('12') == 2
assert decode('12225') == 5
assert decode('1234') == 3

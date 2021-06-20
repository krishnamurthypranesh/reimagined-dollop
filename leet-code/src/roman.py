def romanToInt(s: str) -> int:
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    _sum = 0
    prev = 0
    l = len(s)

    for i in range(l - 1, -1, -1):
        _s = s[i]
        val = numerals[_s]
        if val < prev:
            _sum -= val
        else:
            _sum += val

        prev = val
    return _sum

print(romanToInt('IIII'))
print(romanToInt('LX'))
print(romanToInt('IX'))
print(romanToInt('IV'))

def reverse(x: int) -> int:
    if x in list(range(-9, 10, 1)):
        return x

    orig = x if x > 0 else -x
    _pow = 0

    while orig >= 10 ** _pow:
        _pow += 1

    _pow -= 1
    _sum = 0
    i = _pow

    while i >= 0:
        digit = orig // 10 ** i
        orig -= digit * (10 ** i)
        _sum += digit * 10 ** (_pow - i)
        i -= 1
    if x < 0:
        return -_sum 
    return _sum

print(reverse(123))
print(reverse(-123))
print(reverse(10))
print(reverse(123456789))
print(reverse(1534236469))

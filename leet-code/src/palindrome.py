def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    if x < 10:
        return True
    
    _sum = 0
    _pow = 0

    while x > 10 ** _pow:
        _pow += 1
        
    orig = x
    _pow -= 1
    i = _pow

    while i >= 0:
        digit = orig // 10 ** i
        orig -= digit * (10 ** i)
        _sum += digit * 10 ** (_pow - i)
        i -= 1
        
    if int(_sum) == x:
        return True

    return False


print(isPalindrome(x = 121))

"""
Good morning! Here's your coding interview problem for today.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
"""
from collections import Counter

x = ['waterrfetawx', 'evve', 'rrrrr', '1234321',]

def checkPalindrome(k: int, pat: str) -> bool:
    """
    Algorithm:
    There must be not be odd number of letters. If there are, delete those
    letters and check if the number of letters in the resulting set are 2n
    tuples.

    """

    counts = Counter(pat)
    pat_moded = list(pat)
    new = ''
    limit = k
    idx = 0
    while limit > 0 and idx < len(pat_moded):
        if counts[pat_moded[idx]] % 2 != 0:
            counts[pat[idx]] -= 1
            limit -= 1
        else:
            new += pat_moded[idx]
        idx += 1
    return new == new[::-1]


print(list(map(lambda x: (x, checkPalindrome(1, x)), x)))

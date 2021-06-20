def f(s: str) -> int:
    print(f'Input: {s}')
    dct = dict()
    s_len = len(s)
    curr_max = 0
    max_len = 0
    i = 0
    incr, incl = 1, True

    while i <= len(s) - 1:
        incr, incl = 1, True
        char = s[i]
        print(i, char, dct)
        if dct.get(char, 0):
            print('Resetting counters...')
            dct = dict()

            if curr_max > max_len:
                max_len = curr_max
            curr_max = 0
            
            if s[i - 1] != char:
                print('Resetting to last character')
                incr = -1
                incl = False
    
        i += incr
        if incl:
            dct[char] = 1
            curr_max += 1

    if curr_max > max_len:
        max_len = curr_max

    print('Curr dct', dct)
    return max_len

print('anviaj', f('anviaj'))
# print('abcbbca', f('abcbbca'))
# print('pwwkew', f('pwwkew'))
# print('abcabcbb', f('abcabcbb'))
# print('awwwwa', f('awwwa'))
# print('dvdf', f('dvdf'))
# print('abacba', f('abacba'))
# print('aa', f('aa'))
# print('aab', f('aab'))

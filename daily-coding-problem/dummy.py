from collections import Counter

x = 'evvea'

x_list = list(x)

counts = Counter(x)
limit = 1

for idx, c in enumerate(x_list):
    if counts[c] % 2 != 0:
        if limit >= 0:
            x_list.pop(idx)
            counts[c] -= 1
            limit -= 1

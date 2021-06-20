inp = [[1, 2, 1, 2, 1, 3, 2], [10, 20, 20, 10, 10, 30, 50, 10, 20]]

def sales_by_match(ar):
    stats = dict()

    for i in ar:
        if stats.get(i):
            stats[i] += 1
        else:
            stats[i] = 1

    pairs = 0
    for k, v in stats.items():
        pairs += v // 2

    return pairs

print(list(map(sales_by_match, inp)))

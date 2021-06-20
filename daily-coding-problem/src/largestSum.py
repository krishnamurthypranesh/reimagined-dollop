"""
Logic: The answer is the sum of the largest value and the second largest value
which is not adjacent to it.
"""

from typing import List

def largest_sum(arr: List[int]) -> int:
    ind_val, val_ind = {}, {}

    for idx, a in enumerate(arr):
        ind_val[idx] = a
        val_ind[a] = idx

    arr.sort()



print(largest_sum([2, 4, 6, 2, 5]))
print(largest_sum([5, 1, 1, 5]))

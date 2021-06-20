from typing import List

"""
O(n**2) solution:
    result = []
    for i in range(len(arr)):
        prod = 1
        for j in range(len(arr)):
            if  i != j:
                prod *= arr[j]
        result.append(prod)
"""

def index_product(arr: List[int]) -> List[int]:
    result = []
    for i in range(len(arr)):
        prod = 1
        for j in range(len(arr)):
            if  i != j:
                prod *= arr[j]
        result.append(prod)
    return result

print(index_product([1, 2, 3, 4, 5]))
print(index_product([3, 2, 1]))
print(index_product([1, 2]))

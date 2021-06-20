# array is increasing iff:
#     nums[i] < nums[i + 1]   for all i in (0, len(nums) - 2)
# 
# problem: Find out if array can be turned into increasing by modifying no more
# than one element => n(modifications) == 1
# 
# This is true if there are no more than 


def checkPossibility(nums) -> bool:
    increasing = True
    culprit_count = 0
    avg = sum(nums) / len(nums)

    for n in nums:
        if n <= avg:
            culprit_count += 1

    if culprit_count > 2:
        increasing = False

    return increasing, avg, culprit_count

print(checkPossibility([4, 2, 3]))
print(checkPossibility([4, 2, 1]))
print(checkPossibility([-1, 4, 2, 3]))
print(checkPossibility([3, 4, 2, 3]))

from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum1 = 0

    for i in nums:
        sum1 += i

    return sum1

def get_min(nums: List[int]) -> int:
    min1 = nums[0]

    for i in nums:
        if i < min1:
            min1 = i
    return min1

def get_max(nums: List[int]) -> int:
    max1 = nums[0]

    for i in nums:
        if i > max1:
            max1 = i
    return max1

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))

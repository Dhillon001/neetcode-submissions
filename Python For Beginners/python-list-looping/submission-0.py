from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    nums1 = 0

    for i in range(len(nums)):
        if nums[i] == x:
            nums1 += 1
        else:
            i += 1
    
    return nums1



# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))

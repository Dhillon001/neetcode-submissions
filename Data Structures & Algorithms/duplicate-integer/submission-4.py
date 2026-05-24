
'''Understanding -
    I - an array called nums
    O - Boolean - T/F
    C - If we have negative number in an array
    E - Empty array

Plan - use nested loops, give one element fix position and 
        compare it with other elements, then do same for all the other elements in the list
        this gives us constant space complexity - O(1) but tiem complexity is O(n^2) as this
        is a nexted loop here.

Implement - '''

''' class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True

        return False



Now time for hashmap '''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return 0


"""
    1. for every element, loop through all the other elements, sum and check if it equals target
    2. return both indexes when it does
"""
        
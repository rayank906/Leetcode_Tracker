class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = []
        posSum = [0 for i in range(len(nums))]
        total = 0
        for n in nums:
            preSum.append(total)
            total += n

        total = 0
        
        for i in range(len(nums) - 1, -1, -1):
            posSum[i] = total
            total += nums[i]      
        
        for i in range(len(nums)):
            if posSum[i] == preSum[i]:
                return i
        return -1

"""
    1. make postfix sum for all index
    2. make a prefix sum for all index
    3. loop through nums and compare post and pre, if equal, return idx

    Edge cases:
        a. nothing to l/r
            check validity of l/r before accessing, else use 0
"""
        
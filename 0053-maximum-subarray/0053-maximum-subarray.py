class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for i in range(len(nums)):
            currSum = max(currSum, 0)
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
        return maxSum

"""
    1. keep track of curSum, maxSum
    2. before adding elem, check if sum < 0, if yes reassign curSum to zero
    3. update maxSum to largest of curSum and maxSum
    4. return maxSum
"""
        
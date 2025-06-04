class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmt = 0
        currAmt = 0
        l, r = 0, len(heights) - 1
        while l < r:
            currAmt = (r - l) * min(heights[l], heights[r])
            maxAmt = max(currAmt, maxAmt)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxAmt
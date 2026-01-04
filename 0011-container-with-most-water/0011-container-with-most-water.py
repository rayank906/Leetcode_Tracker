class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
            amt = smallest height * (idx b - idx a)
            1. use two ptrs to the front and back of arr
            2. calc amt and store in max
            3. move ptr with smallest value inwards
            4. return max
        """
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            amt = (r - l) * min(heights[l], heights[r])
            area = max(amt, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return area
        
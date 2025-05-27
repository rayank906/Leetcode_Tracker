class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                curr_profit = max(prices[r] - prices[l], curr_profit)
            else:
                l = r
            r += 1   
        return curr_profit




"""
    Approach: use two ptrs, l & r, that both
"""
        
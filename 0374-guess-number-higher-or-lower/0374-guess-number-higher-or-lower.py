# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n
        while l <= h:
            mid = (l + h) // 2
            if guess(mid) < 0:
                h = mid - 1
            elif guess(mid) > 0:
                l = mid + 1
            else:
                return mid

"""
    1. l = 1, high = n
    2. mid is calculated
    3. if guess(mid) < 0:
        high = mid - 1
    4. if guess(mid) > 0:
        low = mid + 1
    5. else, return mid
"""
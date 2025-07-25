class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

"""
    1. make a hashset of elements
    2. for every element in the hash set, only start a sequence if its
    -1 element doesn't exist
    3. make a count variable
    4. while, num + 1 in set, count += 1
    5. lcs = max(lcs, count)
    6. return lcs

    TimeC: O(n), loop through array once
    SpaceC: O(n) for the extra hashset
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            1. make a set of nums, make a seen set
            2. init maxS = 0
            3. for every num in nums, if num - 1 not in nums, start of a sequence
            3b. currS = 0
            4. while num + currS in set
            5. currS += 1
            6. maxS = max(currS, maxS)
            7. return maxS
        """
        numSet = set(nums)
        maxS = 0
        for num in numSet:
            if num - 1 not in numSet:
                currS = 0
                while num + currS in numSet:
                    currS += 1
                maxS = max(currS, maxS)
        return maxS
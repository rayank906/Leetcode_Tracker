class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs, curSet = [], []
        total = 0
        def helper(i, curSet, total):
            if total == target:
                combs.append(curSet[:])
                return
            if total > target or i >= len(candidates):
                return
            
            # append candidates[i]
            curSet.append(candidates[i])
            total += candidates[i]
            helper(i, curSet, total)

            curSet.pop()
            total -= candidates[i]

            # explore without candidates[i]
            helper(i + 1, curSet, total)
        
        helper(0, curSet, total)
        return combs

"""
    1. create a res array, total variable, currSet array
    2. call our helper with nums, currSet, res, total
        a. if total == target, append copy of curSet to res and return
        b. if total > target, return
        c. append nums[i], explore all the possibilities with that value
        by recursively calling helper with i
        d. pop the nums, explore all possibilities without that value
        by recursively calling helper with i + 1
    3. return combs

    TimeC: O(2^t)
    SpaceC: O(2^t)
"""
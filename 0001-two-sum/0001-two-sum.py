class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
            1. init seen hashmap
            2. for every element
                3. subtract it from target to get remainder for sum
                4. check if remainder exists in seen
                5. if it has, return curr idx and hashmap idx
                6. if its not, add that element to seen 
            
            TC: O(n)
            SC: O(n)
        """
        seen = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in seen:
                return [i, seen[rem]]
            seen[nums[i]] = i
        return [-1, -1]
        
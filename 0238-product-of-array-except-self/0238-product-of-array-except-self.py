class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            1. calculate prefix product and put in res array
                a. keep track of product, init to 1
                b. for num in nums
                c. res[i] = prod
                d. product *= num
            2. calculate suffix product update res array
                a. keep track of product, init to 1
                b. for num in nums, loop in reverse
                c. res[i] *= product
                d. product *= num
            3. return res
        """
        res = [0 for i in range(len(nums))]
        
        # calc prefix
        prod = 1
        for i in range(len(nums)):
            res[i] = prod
            prod *= nums[i]
        # calc suffix
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        return res
        
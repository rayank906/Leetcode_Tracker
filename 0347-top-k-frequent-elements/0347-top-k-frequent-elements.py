class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        occur = defaultdict(int)
        arr = [[] for i in range(len(nums) + 1)]
        for n in nums:
            occur[n] += 1
        for key in occur:
            arr[occur[key]].append(key)
        
        for i in reversed(arr):
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res
        
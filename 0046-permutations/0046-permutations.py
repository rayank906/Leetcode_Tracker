class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            temp = []
            for sublist in res:
                for i in range(len(sublist) + 1):
                    copy = sublist[:]
                    copy.insert(i, num)
                    temp.append(copy)
            res = temp
        return res

"""
    1. starting with an empty list of lists
    1b. for every number in nums,
    2. go through every sublist in lists
    3. loop through all elements + 1 to insert the nums
    into all possible positions
    5. append the resulting arrays to another list of lists
    6. reassign new list to old list after each iteration of sublists
    7. return old list

    TimeC: O(n! * n^2)
    SpaceC: O(n!)
"""
        
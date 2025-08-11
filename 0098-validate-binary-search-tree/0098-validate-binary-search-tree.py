# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)

        for i in range(1, len(res)):
            if res[i - 1] >= res[i]:
                return False
        return True

"""
    1. make a global res array
    2. define a dfs helper
        a. if not root, return
        b. dfs on left subtree
        c. adding node value to the res array
        d. dfs on right subtree
    3. call dfs helper
    4. loop through the array and ensure sorted order by 
    ensuring every value before a value is smaller
"""
        
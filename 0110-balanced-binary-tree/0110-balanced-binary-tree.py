# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

"""
    1. base case: if not root, return None
    Goal: ensure every node is a balanced tree
    1. make a dfs function that traverses nodes from the ground up
    2. for dfs helper, go left and right until base cases. 
    3. return a pair (True, 0) for base case
    bool represents balanced or not, number represents height
    4. recursive step: balanced = balance state of left, right and whether abs(difference) <= 1
    5. return [balanced, 1 + max(l, r) {represents the height calculation}]
    6. call dfs helper and return its boolean value

    TimeC: O(n)
    SpaceC: O(h) where h is the height of the longest subtree
"""
        
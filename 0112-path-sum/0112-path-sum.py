# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val

        if not root.left and not root.right:
            if targetSum == 0:
                return True
            else:
                targetSum += root.val
        
        if self.hasPathSum(root.left, targetSum):
            return True
        if self.hasPathSum(root.right, targetSum):
            return True
        
        return False

"""
    backtracking
    1. Base case: if not root, return None
    2. targetSum - root.val
    3. if not left and not right and targetSum = 0, return True
    4. targetSum + root.val
    5. if hasPathSum(left), True
    6. if hasPathRight(right), True
    7. return False
"""
        
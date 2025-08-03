# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def check(root1, root2):
            if (not root1 and root2) or (not root2 and root1):
                return False
            if not root1 and not root2:
                return True
            
            if root1.val == root2.val:
                return check(root1.left, root2.right) and check(root1.right, root2.left)
            else:
                return False
            
        return check(root.left, root.right)
        

"""
    1. Base cases: if not root, return True
    2. Make a check helper function that takes in two roots
    these would be the opposite subtree nodes.
        a. if they're null return True
        b. if one is null or they're unequal, return False
        c. else, recursively check the left subtree of root1 and right subtree of root2
        and right subtree of root1 and left subtree of root2
    3. call check on left and right subtree

    TimeC: O(n)
    SpaceC: O(h)
"""

        
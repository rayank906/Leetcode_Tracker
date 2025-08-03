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
    1. Base cases: if not root, if not root.left and not root.right, return True
    2. preorder traversal of left subtree (node, left, right)
    3. preorder of right subtree (node, right, left)
    4. return array1 == array2

    TimeC: O(n)
    SpaceC: O(n)
"""

        
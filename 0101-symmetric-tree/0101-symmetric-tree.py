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
        
        array1 = []
        def preorder(root):
            if not root:
                array1.append(-1)
                return
            array1.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        array2 = []
        def preorder2(root):
            if not root:
                array2.append(-1)
                return
            array2.append(root.val)
            preorder2(root.right)
            preorder2(root.left)
        
        preorder(root.left)
        preorder2(root.right)
        
        return array1 == array2

"""
    1. Base cases: if not root, if not root.left and not root.right, return True
    2. preorder traversal of left subtree (node, left, right)
    3. preorder of right subtree (node, right, left)
    4. return array1 == array2
"""

        
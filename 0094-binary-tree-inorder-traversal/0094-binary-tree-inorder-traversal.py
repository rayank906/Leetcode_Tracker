# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traversal(root):
            if not root:
                return None

            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        
        traversal(root)
        return res

"""
    0. make a global res and perform inorder traversal using an inside function
    2. Base case: if not root, return None
    3. inorder(root.left)
    4. res.append(root.val)
    5. inorder(root.right)
"""
        
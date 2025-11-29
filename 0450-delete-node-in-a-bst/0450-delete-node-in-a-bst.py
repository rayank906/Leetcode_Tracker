# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
            1. if not root, return None
            2. search for key using binary search
            3. once found, remove the node
                a. Node has no children
                assign to None
                b. Node has one child
                Replace the node with its child
                c. Node has two children
                Search for minimum in lhs (min helper)
                Replace with that, delete min
            4. return root
        """
        def successorSearch(root):
            while root.right:
                root = root.right
            return root
        
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:     
            if root.left and root.right:
                node = successorSearch(root.left)
                root.val = node.val
                root.left = self.deleteNode(root.left, node.val)
            elif root.right:
                root = root.right
            else:
                root = root.left
        return root
        
        
        
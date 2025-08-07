# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        level = 0
        queue = deque()
        res = []
        temp = []
        
        queue.append(root)
        
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
            res.append(temp if level % 2 != 0 else temp[::-1])
            temp = []
        return res

"""
    1. init level = 0, use temp to store each level
    2. append the root value to a queue
    3. while queue
        a. while len(queue) > 0:
        pop element from queue
        add to temp
        if level is even, append left child then right child
        else, append right child then left child
        
        incr level
        append temp to res
        clear temp
        
    TimeC: O(n^2)
    SpaceC: O(n)
"""
        
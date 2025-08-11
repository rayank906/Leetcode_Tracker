# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

"""
    1. init fast, slow to the head
    2. while fast and fast.next
    3. slow to the next node, fast to next.next
    4. if fast ever meets the slow, return True
    5. if the loop exits, return False
"""
        
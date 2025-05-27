/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head) { return head; }
        
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* temp;

        while (curr) {
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        return prev;
    }
};

/*
    Approach: reverse each link
    1. make prev and curr cursor
    2. keep a link to the next node
    3. reverse current node's link
    4. when curr is null, prev is at the end, which is the new head
    5. return prev
*/

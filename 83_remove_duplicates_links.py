"""
LeetCode#83
Given the head of a sorted linked list, delete all duplicates 
such that each element appears only once. 
Return the linked list sorted as well.
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)
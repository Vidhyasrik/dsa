"""
LeetCode#19
Given the head of a singly linked list, we need to remove the nth node from the end of list and return its head.
"""

def removeNthFromChild(head, n):
    slow = head
    fast = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
        slow.next = slow.next.next
    return head
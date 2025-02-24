"""
LeetCode#19
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remNL(head, n):
    """
    Removes the nth node from the end of a linked list.
    Args:
        head: The head of the linked list.
        n: The position of the node to remove from the end.
    Returns:
        The head of the modified linked list.
    """

    if not head:
        return None

    fast, slow = head, head
    for _ in range(n):
        if not fast: # handles the case where n is larger than the list length.
            return head.next # if n is equal to the length of the list, remove head.
        fast = fast.next

    if not fast: # handles the case where n is equal to the length of the list.
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head
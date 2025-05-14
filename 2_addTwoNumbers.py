"""
LeetCode#2
ou are given two non-empty linked lists representing 
two non-negative integers. The digits are stored in reverse order 
and each of their nodes contain a singlThe digits are stored in 
reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    Adds two numbers represented as linked lists.

    Args:
        l1: The head of the first linked list.
        l2: The head of the second linked list.

    Returns:
        The head of the linked list representing the sum.
    """
    dummy_head = ListNode(0)  # Dummy head to simplify the code
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sum_val = x + y + carry

        carry = sum_val // 10
        current.next = ListNode(sum_val % 10)

        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next
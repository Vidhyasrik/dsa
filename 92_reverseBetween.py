"""
LeetCode#92
Given the head of a singly linked list and two integers 
left and right where left <= right, reverse the nodes of 
the list from position left to position right, and return the reversed list.
"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Node, left: int, right: int) -> Node:
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = head
        for _ in range(left-1):
            prev = prev.next

        curr = prev.next
        next_node = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = next_node
            next_node = curr
            curr = temp
        prev.next.next = curr
        prev.next = next_node

        return dummy.next


arr = [1, 2, 3, 4, 5]
left = 2
right = 4


def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for i in arr:
        current.next = ListNode(arr[i])
        current = current.next
    return head


def linkedlist_to_head(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result







"""
LeetCode#206
"""
def reverseLinkedList(head):
    node = None
    while head:
        temp = head.next
        head.next = node
        node = head
        head = temp
    return node
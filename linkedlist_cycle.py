"""
LeetCode#141
"""
def has_cycle(head):
    fast=slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return True
    return False
"""
LeetCode#21
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made 
by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify the process of merging the two lists
        dummy = ListNode()
        current = dummy
        # Continue the process until one of the lists is exhausted
        while list1 and list2:
            # Compare the values of the current nodes in the two lists
            if list1.val < list2.val:
                # If the value of the current node in list1 is smaller, append it to the merged
                # list and move to the next node in list1
                current.next = list1
                list1 = list1.next
            else:
                # If the value of the current node in list2 is smaller, append it to the merged
                # list and move to the next node in list2
                current.next = list2
                list2 = list2.next
                # Move to the next node in the merged list
            current = current.next
            # If list1 is not exhausted, append all its nodes to the merged list
            # If list1 is not exhausted, append all its nodes to the merged list
            if list1:
                current.next = list1
            elif list2:
                current.next = list2
                # Return the head of the merged list
            return dummy.next

#Example usage:
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head 

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

list1_values = [1, 2, 4]
list2_values = [1, 3, 4]

list1 = create_linked_list(list1_values)
list2 = create_linked_list(list2_values)

merged_list = Solution().mergeTwoLists(list1, list2)

print(linked_list_to_list(merged_list)) 




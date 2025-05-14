"""
LeetCode#23
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Method#1
def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    lists = [l for l in lists if l]
    # Create a min heap to store the nodes of the linked lists
    min_heap = []
    for i, node in enumerate(lists):
        min_heap.append((node.val, i, node))
    heapq.heapify(min_heap)
    result = ListNode()
    current = result
    while min_heap:
        # Pop the node with the smallest value from the heap
        val, i, node = heapq.heappop(min_heap)
        # Add the node to the result linked list
        current.next = node
        current = current.next
        # If the popped node has a next node, push it into the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
    return result.next

# Method#2
# def mergeKLists(lists):
#     """
#     Merges k sorted linked lists into one sorted linked list.

#     Args:
#         lists: A list of sorted linked list heads.

#     Returns:
#         The head of the merged sorted linked list.
#     """

#     if not lists:
#         return None

#     def merge_two_lists(list1, list2):
#         dummy = ListNode()
#         current = dummy
#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next
#         if list1:
#             current.next = list1
#         elif list2:
#             current.next = list2
#         return dummy.next

#     def merge_lists(lists, start, end):
#         if start == end:
#             return lists[start]
#         if start > end:
#             return None
#         mid = (start + end) // 2
#         left = merge_lists(lists, start, mid)
#         right = merge_lists(lists, mid + 1, end)
#         return merge_two_lists(left, right)

#     return merge_lists(lists, 0, len(lists) - 1)

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

list1_values = [1, 4, 5]
list2_values = [1, 3, 4]
list3_values = [2, 6]

list1 = create_linked_list(list1_values)
list2 = create_linked_list(list2_values)
list3 = create_linked_list(list3_values)

lists = [list1, list2, list3]
print("lists:", [i.__dict__ for i in lists])

merged_list = mergeKLists(lists)

print(linked_list_to_list(merged_list))






                
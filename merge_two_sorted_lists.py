#LeetCode#21
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=next
class Merge_Two_Sorted_Lists:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode()
        current=dummy
        while l1 and l2:
            if l1.val<l2.val:
                current.next=l1
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next
        current.next = l1 or l2
        return head.next
l1=[1,2,4]
l2=[1,3,4]
print(Merge_Two_Sorted_Lists().mergeTwoLists(l1,l2))
# print("result:", Merge_Two_Sorted_Lists().mergeTwoLists(l1,l2))

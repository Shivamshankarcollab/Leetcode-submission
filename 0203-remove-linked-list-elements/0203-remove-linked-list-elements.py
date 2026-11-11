# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        backward = dummy
        current = head
        while(current != None):
            if current.val == val:
                forward = current.next
                backward.next = forward
                current = forward
            else:
                backward = current
                current = current.next
        return dummy.next

        
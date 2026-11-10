# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0 
        temp = head 
        while temp != None:
            count +=1
            temp = temp.next
        middle = count // 2
        current = head
        for i in range(middle):
            current = current.next
        return current
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        res = ListNode()
        a = res
        while l1 and l2:
            temp = l1.val + l2.val + extra
            extra = temp//10
            a.next = ListNode(temp%10)
            a = a.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            a.next = ListNode((l1.val+extra)%10)
            extra = (l1.val+extra)//10
            l1 = l1.next
            a = a.next
        while l2:
            a.next = ListNode((l2.val+extra)%10)
            extra = (l2.val+extra)//10
            l2 = l2.next
            a = a.next
        if extra:
            a.next = ListNode(extra)
        return res.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        new = ListNode(0)
        r = new
        
        while p and q:
            if p.val>q.val:
                r.next = ListNode(q.val)
                q = q.next
                r = r.next
            else:
                r.next = ListNode(p.val)
                p = p.next
                r = r.next
        while p:
            r.next = ListNode(p.val)
            p = p.next
            r = r.next
        while q:
            r.next = ListNode(q.val)
            q = q.next
            r = r.next
            
        return new.next
            
        
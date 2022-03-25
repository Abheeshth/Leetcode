# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        p = head  
        while p:
            p = p.next
            length +=1
        print(length)
        first = length-n
        # for first node
        if first == 0:
            return head.next
        # for last node
        if n == length:
            q = head
            while q.next:
                q = q.next
            q.next = None
            return head
        else:
            q = head 
            for i in range(first-1):
                q = q.next
            q.next = q.next.next
            return head
            
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        elif head != None and head.next == None:
            return head
        
        else:
            p = head

            while p.next:
                n = p.next
                p.next = n.next
                n.next = head
                head = n
            
            return head
        
        
# OR

class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head

        n = head.next
        h = self.reverseList(n)

        # reverse link
        head.next = None
        n.next = head

        return h
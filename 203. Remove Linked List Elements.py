# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        elif head != None and head.next == None:
            if head.val == val:
                return None
            else:
                return head
        else:
            dummy = ListNode(next=head)
            prev, curr = dummy, head

            while curr:
                if curr.val == val:
                    prev.next = curr.next
                else:
                    prev = curr
                    
                curr = curr.next

            return dummy.next
                    
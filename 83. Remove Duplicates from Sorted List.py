# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        elif head != None and head.next == None:
            return head
        else:
            curr = head

            while curr != None:
                while curr.next != None and curr.next.val == curr.val:
                    curr.next = curr.next.next
                curr = curr.next

            return head
                    
        
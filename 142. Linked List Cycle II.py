# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        else:
            fast = head
            slow = head

            has_cycle = False
            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    has_cycle = True
                    break
            
            if has_cycle == False:
                return None

            slow = head
            while slow != fast:
                slow = slow.next 
                fast = fast.next
            
            return slow
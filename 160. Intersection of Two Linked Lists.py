# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None and headB == None:
            return None
        elif headA == None and headB != None:
            return None
        elif headA != None and headB == None:
            return None
        else:
            currentA = headA
            currentB = headB
            len_a = 0
            len_b = 0

            while currentA != None:
                currentA = currentA.next
                len_a += 1

            while currentB != None:
                currentB = currentB.next
                len_b += 1

            diff = 0
            if len_a > len_b:
                diff = len_a - len_b
                currentA = headA
                currentB = headB
            else:
                diff = len_b - len_a
                currentA = headB
                currentB = headA

            count = 0
            while count < diff:
                currentA = currentA.next
                count += 1

            while currentA != None and currentB != None:
                if currentA == currentB:
                    return currentA
                else:
                    currentA = currentA.next
                    currentB = currentB.next
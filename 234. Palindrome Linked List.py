# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return True
        elif head != None and head.next == None:
            return True
        else:
            fast = head
            slow = head

            # find the middle (with slow pointer)
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            # reverse second half
            prev = None
            while slow:
                tmp = slow.next
                slow.next = prev
                prev = slow
                slow = tmp

            # check palindrome
            left, right = head, prev
            while right:
                if left.val != right.val:
                    return False
                
                left = left.next
                right = right.next
            return True

        # array solution
    """ nums = []

        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0

        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True """
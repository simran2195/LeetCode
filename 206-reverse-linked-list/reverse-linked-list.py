# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # O(n) time complexity
        #  Iterative
        
        # prev, curr = None, head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt

        # return prev

        # Recursive
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head # reverse the link
        
        head.next = None
        return newHead


        
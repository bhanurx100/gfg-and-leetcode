# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Step 1: Split the list into two halves using the slow and fast pointer technique
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next  # Midpoint to split the list
        slow.next = None  # Break the list into two halves

        # Step 2: Recursively sort each half
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        # Dummy node to simplify merging logic
        dummy = ListNode(0)
        current = dummy

        # Merge nodes from both halves
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        # Attach remaining nodes from either half
        if left:
            current.next = left
        if right:
            current.next = right

        return dummy.next
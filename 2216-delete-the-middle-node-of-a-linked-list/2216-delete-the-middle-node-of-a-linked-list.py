# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        # Initialize two pointers
        slow = head
        fast = head.next.next

        # Traverse the list until fast reaches the end
        while fast and fast.next:
            slow = slow.next       # Move slow one step
            fast = fast.next.next  # Move fast two steps

        # Delete the middle node by skipping it
        slow.next = slow.next.next

        # Return the head of the modified list
        return head

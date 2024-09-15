# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Function to delete a node from a singly linked list
    def deleteNode(self, node: ListNode) -> None:
        # Store the next node's pointer temporarily
        nextNode = node.next.next
        # Copy the value of the next node to the current node
        node.val = node.next.val
        # Update the next pointer to skip the next node
        node.next = nextNode
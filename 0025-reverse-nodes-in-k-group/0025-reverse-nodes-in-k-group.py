# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses nodes of a linked list in groups of size k.

        Parameters:
            head (ListNode): The head of the linked list.
            k (int): The size of the groups to reverse.

        Returns:
            ListNode: The head of the modified linked list.
        """
        def reverseLinkedList(temp):
            """
            Helper function to reverse a linked list segment.
            
            Parameters:
                temp (ListNode): The head of the segment to reverse.
            
            Returns:
                ListNode: The new head of the reversed segment.
            """
            prevnode = None
            while temp:
                nextnode = temp.next
                temp.next = prevnode
                prevnode = temp
                temp = nextnode
            return prevnode

        def getKthNode(temp, k):
            """
            Finds the k-th node from the start node.
            
            Parameters:
                temp (ListNode): The starting node.
                k (int): The position to find.
            
            Returns:
                ListNode: The k-th node or None if the list is shorter than k.
            """
            for _ in range(k - 1):
                if not temp:
                    return None
                temp = temp.next
            return temp

        dummy = ListNode(0)  # Dummy node to simplify edge cases
        dummy.next = head
        prevnode = dummy  # Pointer to the last node of the previous group

        while True:
            kth_node = getKthNode(prevnode.next, k)  # Find the k-th node
            if not kth_node:
                break  # If fewer than k nodes remain, stop

            nextnode = kth_node.next  # The node after the k-th node
            # Reverse the current group
            current = prevnode.next
            kth_node.next = None  # Temporarily break the link
            reversed_head = reverseLinkedList(current)
            
            # Connect the reversed group back
            prevnode.next = reversed_head
            current.next = nextnode  # Connect the group's tail to the next part

            # Move prevnode to the end of the current group
            prevnode = current

        return dummy.next  # Return the new head of the modified list

class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        current = head

    # Traverse the doubly linked list
        while current is not None and current.next is not None:
            # Check if the current node and the next node have the same value
            if current.data == current.next.data:
                # Save the reference to the node after the duplicate
                nextnode = current.next.next
                
                # Remove the duplicate by updating the current node's next pointer
                current.next = nextnode
                
                # If there is a nextnode, update its prev pointer
                if nextnode:
                    nextnode.prev = current
            else:
                # Move to the next node
                current = current.next
    
        return head
    
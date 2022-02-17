"""
Problem 23 - Merge k Sorted Lists
Difficulty: Hard
URL: https://leetcode.com/problems/merge-k-sorted-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Remove empty lists
        lists = [l for l in lists if l]
        if not lists:
            return None

        # Instantiate the linked list
        ptr = ListNode()
        head = ptr

        while True:
            # Loop until no lists remain
            if not len(lists):
                break
            
            # Find the minimum value and index
            min_idx = 0
            min_val = lists[min_idx].val
            for i in range(1, len(lists)):
                if lists[min_idx] and lists[i].val < min_val:
                    min_idx = i
                    min_val = lists[i].val

            # Remove the node from the list with the min
            if lists[min_idx].next:
                lists[min_idx] = lists[min_idx].next
            # Remove the newly empty list from the lists
            else:
                lists.pop(min_idx)

            # Update the new list
            ptr.val = min_val
            # Create the next node in the list if there are still values remaining
            if len(lists):
                ptr.next = ListNode()
                ptr = ptr.next
        
        return head

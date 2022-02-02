# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1 = []
        a2 = []
        while l1 != None:
            a1.append(str(l1.val))
            l1 = l1.next
        while l2 != None:
            a2.append(str(l2.val))
            l2 = l2.next
        
        n1 = int("".join(reversed(a1)))
        n2 = int("".join(reversed(a2)))
        
        sum_ = str(n1 + n2)
        # print(sum_)
        
        for i in range(len(sum_)):
            if i == 0:
                node = ListNode(val=int(sum_[i]))
            else:
                node = ListNode(val=int(sum_[i]), next=node)
        
        return node


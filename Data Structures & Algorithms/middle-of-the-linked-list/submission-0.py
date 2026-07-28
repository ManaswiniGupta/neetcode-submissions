# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=head
        f=head
        curr=head.next
        while f and f.next.next:
            s=curr.next
            f=curr.next.next
            curr=curr.next
        return s
        
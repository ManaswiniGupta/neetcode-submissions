# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        for i in range(k):
            curr=head
            while curr.next.next:
                curr=curr.next
            nh=curr.next
            nh.next=head
            curr.next=None
            head=nh
        return head

        
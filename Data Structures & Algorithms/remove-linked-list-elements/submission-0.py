# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        curr=head
        while head and head.val == val:
            head = head.next
        while curr and curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
            curr=curr.next
        return head

        
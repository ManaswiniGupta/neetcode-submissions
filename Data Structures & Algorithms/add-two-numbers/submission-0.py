# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=0
        b=0
        c=l1
        d=l2
        while c:
            a=a*10+c.val
            
            c=c.next
        while d:
            b=b*10+d.val
            d=d.next
        a=(int(str(a)[::-1])+int(str(b)[::-1]))
        # print(a)
        k=ListNode()
        f=k
        while a>0:
            g=a%10
            a=a//10
            f.next=ListNode(g)
            f=f.next
            
        return k.next

        

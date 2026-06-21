# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = ListNode(0,head)
        i = k
        j = k
        for _ in range(n+1):
            j = j.next
        while j :
            i = i.next
            j = j.next
        i.next = i.next.next
        return k.next

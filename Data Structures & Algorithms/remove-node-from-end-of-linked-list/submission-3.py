# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        curr = head
        list_len = 0

        while curr:
            list_len += 1
            curr = curr.next
        
        remove_no = list_len - n

        if remove_no == 0:
            return head.next

        temp = head
        pos = 0
        while temp and temp.next:
            if pos == remove_no - 1:
                temp.next = temp.next.next

            temp = temp.next
            pos += 1

        return head
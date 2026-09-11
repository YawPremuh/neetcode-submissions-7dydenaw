# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_list = []
    
        curr = head
        while curr:
            node_list.append(curr.val)
            curr = curr.next

        if not node_list:
            return

        curr = head
        l = 1
        r = len(node_list) - 1

        for i in range(1, len(node_list)):

            if i % 2 != 0:
                curr.next = ListNode(node_list[r])
                curr = curr.next
                r -= 1
            else:
                curr.next = ListNode(node_list[l])
                curr = curr.next
                l += 1

            curr.next = None


        


        
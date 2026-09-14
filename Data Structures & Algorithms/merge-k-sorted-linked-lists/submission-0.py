# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node_list = []

        for head in lists:
            curr = head

            while curr:
                node_list.append(curr.val)
                curr = curr.next

        if not node_list:
            return None

        node_list.sort()

        newList = ListNode(node_list[0])
        curr = newList

        for i in range(1, len(node_list)):
            curr.next = ListNode(node_list[i])
            curr = curr.next

        return newList
        
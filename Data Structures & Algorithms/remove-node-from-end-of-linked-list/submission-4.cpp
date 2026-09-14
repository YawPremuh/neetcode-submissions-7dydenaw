/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!head){
            return nullptr;
        }

        ListNode* curr = head;
        int list_len = 0;

        while (curr){
            list_len++;
            curr = curr->next;
        }

        int remove_no = list_len - n;

        if (remove_no == 0){
            return head->next;
        }

        ListNode* temp = head;
        int pos = 0;

        while (temp && temp->next){
            if (pos == remove_no - 1){
                temp->next = temp->next->next;
                break;
            }
            temp = temp->next;
            pos++;
        }

        return head;

    }
};

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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int> node_list;

        for (ListNode* linked_lst : lists){
            ListNode* curr = linked_lst;

            while (curr){
                node_list.push_back(curr->val);
                curr = curr->next;
            }
        };

        if (node_list.empty()){
            return nullptr;
        }

        sort(node_list.begin(), node_list.end());

        ListNode* newList = new ListNode(node_list[0]);
        ListNode* curr = newList;

        for (int i = 1; i < node_list.size(); i++){
            curr->next = new ListNode(node_list[i]);
            curr = curr->next;
        };

        return newList;
    }
};

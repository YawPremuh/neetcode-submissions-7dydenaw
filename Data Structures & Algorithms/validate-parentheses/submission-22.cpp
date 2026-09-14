class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> brackets = {
            {']' , '['},
            {'}' , '{'},
            {')' , '('},
        };

        for (char ch : s){
            if (ch == '[' || ch == '{' || ch == '('){
                st.push(ch);
            }

            else if (!st.empty() && brackets[ch] == st.top()){
                st.pop();
            }

            else{
                return false;
            }
        }

        return st.empty();
    }
};

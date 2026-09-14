class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> res;

        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++){
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }

            int l = i + 1;
            int r = nums.size() - 1;

            while (l < r){
                int threesum = nums[i] + nums[l] + nums[r];

                if (threesum == 0){
                    vector <int> triplets = {
                        nums[i],
                        nums[l],
                        nums[r]
                    };

                    res.insert(triplets);
                    l++;
                    r--;

                    while(l < r && nums[l] == nums[l-1]){
                        l++;
                    }

                    while(l < r && nums[r] == nums[r+1]){
                        r--;
                    }
                }
                else if (threesum < 0){
                    l++;
                }
                else{
                    r--;
                }
            }
        }
        return vector<vector<int>>(res.begin(), res.end());
    }
};

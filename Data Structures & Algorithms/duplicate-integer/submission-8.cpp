class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> a1;
        // a1 = sort(nums.begin(), nums.end());
        for(auto n : nums)
        {
            if(a1.count(n))
                return true;
            else
                a1.insert(n);
                
        }
        return false;

        

    }
};
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int, int> tmp;
        vector<int> a = {1,2};
        vector<int> ans;
        for(int num : nums)
        {
            tmp[num]++;
        }
        vector<pair<int,int>> vec (tmp.begin(), tmp.end());
        sort(vec.begin(), vec.end(), [](const pair<int, int>& a, const pair<int, int>& b) 
        {
            return a.second > b.second; 
        });

        for(int i=0;i<k;i++){
            ans.push_back(vec[i].first);
        }

        // for (const auto& p : vec) {
        //     // p 是一個 pair，所以要印出 p.first 和 p.second
        //     std::cout << "Key: " << p.first << ", Value: " << p.second << std::endl;
        // }

        return ans;

    }
};

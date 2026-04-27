class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        if(strs.size()==1 && strs[0]=="") 
        {
            return {{""}};
        }
        else if(strs.size()==1)
        {
            return {{strs[0]}};
        }
        else
        {
            unordered_map<string, vector<string>> groups;
            for (string i : strs)
            {
                string tmp = i;
                sort(tmp.begin(), tmp.end());
                groups[tmp].push_back(i);
            }
            vector<vector<string>> result;
            for (auto& [key, group] : groups)
            {
                result.push_back(group);
            }
            return result;
        }
    }
};

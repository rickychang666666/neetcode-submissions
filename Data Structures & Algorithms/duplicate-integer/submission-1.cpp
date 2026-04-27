class Solution {
public:

    bool hasDuplicate(vector<int>& nums) {
        int flag = 0;
        if(nums.size()==0)
        {
            return false;
        }
        for(int i = 0;i<nums.size()-1;i++)
        {
            for(int j=i+1;j<nums.size();j++)
            {
                // cout<<"array i: "<<nums[i]<<endl;
                // cout<<"array j: "<<nums[j]<<endl;
                if(nums[i]==nums[j])
                {
                    flag = 1;
                    return true;
                }
            }
        }

        if (flag==0)
        {
            return false;
        }
    }
};
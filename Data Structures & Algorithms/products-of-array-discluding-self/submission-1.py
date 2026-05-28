class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=1
        ans=[]
        flag=0
        if nums.count(0) > 1:
            for i in range(len(nums)):
                ans.append(0)
            return ans
        
        for tmp in nums:
            if tmp == 0:
                flag=1
                continue
            else:
                total *= tmp
        for i in range(len(nums)):
            if nums[i]==0:
                ans.append(total)
            elif flag==1:
                ans.append(0)
            else:
                ans.append(int(total / nums[i]))
        return ans
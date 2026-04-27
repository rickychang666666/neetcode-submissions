class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        tmp = ""
        for i in strs:
            tmp+=(str(len(i)) + "#" + i)
        return tmp
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        flag=0    
        tmp=""
        ans=[]
        size=len(s)
        while flag < size:
            j=flag
            while s[j] != "#":
                j+=1
            length = int(s[flag:j]) #might be more than one digit
            ans.append(s[j+1:j+length+1])

            flag = j+length+1

        return ans
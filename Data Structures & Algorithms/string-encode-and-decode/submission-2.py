class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        tmp = ""
        for i in strs:
            tmp+=(i+"~")
        return tmp
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        tmp=""
        ans=[]
        size=len(s)
        for i in range(size):
            if s[i]!="~":
                tmp+=s[i]
            else:
                ans.append(tmp)
                tmp=""
        return ans
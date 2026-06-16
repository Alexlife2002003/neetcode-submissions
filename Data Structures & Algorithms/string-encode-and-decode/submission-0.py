class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for word in strs:
            n=len(word)
            res+=f"{n}#{word}"
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        left=0
        right=0
        while right<len(s):
            while s[right]!="#":
                right+=1
            
            length=int(s[left:right])
            left=right+1
            right=left+length
            res.append(s[left:right])
            left=right
        
        return res

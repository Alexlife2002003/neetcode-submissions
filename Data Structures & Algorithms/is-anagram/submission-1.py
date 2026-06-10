class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        countT=defaultdict(int)
        countS=defaultdict(int)

        for i in range(len(s)):
            countT[t[i]]+=1
            countS[s[i]]+=1
        
        return countT==countS
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def dfs(i, suma, sub):
            if suma==target:
                result.append(sub.copy())
                return
            
            if i==len(candidates) or suma>target:
                return 
            
            sub.append(candidates[i])
            dfs(i+1, suma+candidates[i], sub)

            sub.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            
            dfs(i+1, suma, sub)
        

        dfs(0,0,[])
        return result
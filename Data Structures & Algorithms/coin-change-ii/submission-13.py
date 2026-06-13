class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def dfs(i, suma):
            if suma==amount:
                return 1
            
            if i==len(coins) or suma>amount:
                return 0
            
            if (i, suma) in memo:
                return memo[(i, suma)]
            
            take = dfs(i, suma+coins[i])
            skip = dfs(i+1, suma)
            memo[(i,suma)]=take+skip
            return memo[(i, suma)]
        
        return dfs(0,0)
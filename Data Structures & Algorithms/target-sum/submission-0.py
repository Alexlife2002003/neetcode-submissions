class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, suma):
            if i==len(nums):
                return 1 if suma==target else 0
            
            addition=dfs(i+1, suma+nums[i])
            substract=dfs(i+1, suma-nums[i])

            return addition+substract
        
        return dfs(0,0)
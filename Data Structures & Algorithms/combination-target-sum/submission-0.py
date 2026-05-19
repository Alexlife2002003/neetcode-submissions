class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        def dfs(i, sub, total):
            if total==target:
                result.append(sub.copy())
                return
            
            if i>=len(nums) or total>target:
                return
            
            sub.append(nums[i])
            dfs(i,sub,total+nums[i])

            sub.pop()
            dfs(i+1, sub, total)
        dfs(0,[],0)
        return result
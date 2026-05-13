class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(i,sub):
            if i>=len(nums):
                result.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i+1, sub)

            sub.pop()
            dfs(i+1,sub)
        
        dfs(0,[])
        return result
        
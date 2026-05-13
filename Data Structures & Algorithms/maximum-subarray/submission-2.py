class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub=nums[0]
        cur_sub=0

        for num in nums:
            if cur_sub<0:
                cur_sub=0

            cur_sub+=num
            max_sub=max(max_sub, cur_sub)
        
        return max_sub

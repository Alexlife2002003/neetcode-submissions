class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        seen=set(nums)
        for num in nums:
            cur=num
            cur_length=0
            while cur in seen:
                cur+=1
                cur_length+=1
            res=max(res, cur_length)
        return res
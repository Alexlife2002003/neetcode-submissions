class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest=0

        for num in nums:
            streak=0
            cur=num
            while cur in seen:
                streak+=1
                cur+=1
            longest=max(longest, streak)
        return longest
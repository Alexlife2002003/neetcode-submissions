class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=0
        intervals.sort()
        lastend=intervals[0][1]
       # 1,2 1, 4
        for start, end in intervals[1:]:
            if start<lastend:
                lastend=min(end, lastend)
                res+=1
            else:
                lastend=end
        return res

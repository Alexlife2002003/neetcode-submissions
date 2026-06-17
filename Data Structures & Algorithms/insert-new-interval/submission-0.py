class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        res=[]

        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
            else:
                mininum=min(newInterval[0], intervals[i][0])
                maximum=max(newInterval[1], intervals[i][1])
                newInterval=[mininum, maximum]
        
        res.append(newInterval)
        return res
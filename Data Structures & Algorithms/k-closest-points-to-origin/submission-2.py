class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]

        for i in range(len(points)):
            x, y = points[i]
            
            dist = (x*x)+(y*y)
            heapq.heappush(heap, [-dist, x, y])
            if len(heap)>k:
                heapq.heappop(heap)
        
        res=[]

        while heap:
            dist, x, y= heapq.heappop(heap)
            res.append((x,y))
        
        return res
            

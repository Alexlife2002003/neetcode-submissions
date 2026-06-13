class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap=[(0,0)]
        edges=defaultdict(list)
        visited=set()
        res=0
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2=points[j]
                dist= abs(x1-x2)+abs(y1-y2)
                edges[i].append([dist, j])
                edges[j].append([dist, i])
        
        while heap:
            cost1, i1= heapq.heappop(heap)
            if i1 in visited:
                continue
            
            visited.add(i1)
            res+=cost1
            for cost2, i2 in edges[i1]:
                if i2 not in visited:
                    heapq.heappush(heap, [cost2, i2])
        return res


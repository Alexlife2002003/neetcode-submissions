class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap=[(0,0)]
        edges = defaultdict(list)

        for i in range(len(points)):
            x1, y1= points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                dist = abs(x1-x2)+ abs(y1-y2)
                edges[i].append([dist, j])
                edges[j].append([dist, i])
        
        res=0
        visit=set()
        result=0

        while len(visit)<len(points):
            cost, point = heapq.heappop(minheap)
            if point in visit:
                continue
            result+=cost
            visit.add(point)
            for nei, i in edges[point]:
                if i not in visit:
                    heapq.heappush(minheap,[nei, i])
        
        return result
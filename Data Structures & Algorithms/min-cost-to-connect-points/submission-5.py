class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges=defaultdict(list)
        heap=[(0,0)] # dist , node
        for i in range(len(points)):
            x1, y1= points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                dist = abs(x1-x2)+abs(y1-y2)
                edges[i].append([dist, j])
                edges[j].append([dist, i])
        visit=set()
        res=0
        while heap:
            cost1, node1 = heapq.heappop(heap)
            if node1 in visit:
                continue
            res+=cost1
            visit.add(node1)

            for cost2, node2 in edges[node1]:
                if node2 not in visit:
                    heapq.heappush(heap, (cost2, node2))
        
        return res

            


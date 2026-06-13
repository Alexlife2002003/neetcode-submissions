class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)

        adj=defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res =0
        visit=set()
        minheap=[(0,0)] #cost goes first

        while len(visit)<n:
            cost, i = heapq.heappop(minheap)

            if i in visit:
                continue
            
            res+=cost
            visit.add(i)

            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minheap, [neiCost, nei])
        
        return res

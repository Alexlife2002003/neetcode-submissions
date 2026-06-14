class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols= len(grid), len(grid[0])
        q=deque()
        visit=set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    visit.add((r,c))
                    q.append((r,c))
        
        def addLand(r, c):
            if r<0 or c<0 or r==rows or c==cols:
                return 
            
            if (r,c) in visit or grid[r][c]==-1:
                return 
            
            visit.add((r,c))
            q.append((r,c))
            
        dist=0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                grid[r][c]=dist
                addLand(r+1,c)
                addLand(r,c+1)
                addLand(r-1,c)
                addLand(r,c-1)
            dist+=1
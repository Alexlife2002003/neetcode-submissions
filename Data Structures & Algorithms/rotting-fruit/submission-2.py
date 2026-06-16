class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res=-1
        rows, cols = len(grid), len(grid[0])
        q=deque()
        freshOranges=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append([r,c])
                if grid[r][c]==1:
                    freshOranges+=1
        if freshOranges==0:
            return 0
        def addFruit(r, c):
            nonlocal freshOranges
            if r<0 or c<0 or r==rows or c==cols:
                return 
            
            if grid[r][c]!=1:
                return 
            
            grid[r][c]=2
            q.append((r,c))
            freshOranges-=1


        while q:
            for i in range(len(q)):
                r,c=q.popleft()

                addFruit(r+1, c)
                addFruit(r, c+1)
                addFruit(r-1, c)
                addFruit(r, c-1)
            
            res+=1

        return res if freshOranges==0 else -1
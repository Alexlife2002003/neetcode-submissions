class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows-1

        while top<=bottom:
            row=(top+bottom)//2

            if matrix[row][0]>target:
                bottom-=1
            elif matrix[row][-1]<target:
                top+=1
            else:
                break
        
        if not top<=bottom:
            return False
        
        row=(top+bottom)//2

        left,right =0, cols-1

        while left<=right:
            mid=(left+right)//2

            if matrix[row][mid]<target:
                left+=1
            elif matrix[row][mid]>target:
                right-=1
            else:
                return True

        return False
        

        

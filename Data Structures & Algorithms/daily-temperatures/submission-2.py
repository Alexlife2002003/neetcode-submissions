class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[] # i, temp
        result = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp>stack[-1][1]:
                i2, temp2= stack.pop()
                result[i2]=i-i2
            
            stack.append([i, temp])
        
        return result
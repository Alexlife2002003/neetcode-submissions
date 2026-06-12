class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            # go right
            result += matrix.pop(0)

            # go down
            if matrix and matrix[0]:
                for row in matrix:
                    if row:
                        result.append(row.pop())

            # go left
            if matrix:
                result += matrix.pop()[::-1]

            # go up
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    if row:
                        result.append(row.pop(0))

            # remove empty rows
            matrix = [row for row in matrix if row]

        return result
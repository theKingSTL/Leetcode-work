class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        
        while matrix:
            result.extend(matrix.pop(0)) 
            
            if not matrix: 
                break
            
            for row in matrix:
                if row: 
                    result.append(row.pop(-1))
            
            if not matrix or not matrix[0]:
                break
            
            if matrix:
                result.extend(reversed(matrix.pop(-1)))
            
            for row in reversed(matrix):
                if row:
                    result.append(row.pop(0))
        
        return result

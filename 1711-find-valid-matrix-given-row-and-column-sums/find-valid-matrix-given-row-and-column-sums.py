class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        num_rows = len(rowSum)
        num_cols = len(colSum)
        
        # Initialize the matrix with zeros
        matrix = [[0] * num_cols for _ in range(num_rows)]
        
        # Fill the matrix with the required values
        for i in range(num_rows):
            for j in range(num_cols):
                # Find the minimum value to put in the cell [i][j]
                val = min(rowSum[i], colSum[j])
                matrix[i][j] = val
                
                # Subtract the value from the row and column sums
                rowSum[i] -= val
                colSum[j] -= val
    
        return matrix

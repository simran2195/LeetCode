class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_rows = [min(row) for row in matrix]
        max_in_cols = [max(col) for col in zip(*matrix)]
        
        lucky_numbers = []
        
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == min_in_rows[i] and value == max_in_cols[j]:
                    lucky_numbers.append(value)

        return lucky_numbers
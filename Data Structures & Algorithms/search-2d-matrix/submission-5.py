"""
Understand:
input: 
- matrix
    - list of lists containing ints
    - each sub list is same length.
    - sorted in inc. order
    - first int in every sublist is greater than the last int in previous list
- target (int)

output: bool repping if target is in the matrix

Plan:

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m*n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
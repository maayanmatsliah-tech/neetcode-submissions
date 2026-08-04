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
        mtrx_len = len(matrix) - 1
        # pointer to sublist in matrix
        mtrx_p = 0
        # pointers within sublist
        s, e = 0, len(matrix[0]) - 1

        while s <= e:
            # recalculate m in every iteration
            m = (e - s) // 2 + s
            # sublist
            lst = matrix[mtrx_p]

            if target == lst[m]:
                return True
            elif target > lst[e]:
                if mtrx_p == mtrx_len:
                    return False
                mtrx_p +=1
            elif target < lst[s]:
                return False
            elif target > lst[m]:
                s = m + 1
            else:
                e = m - 1
        return False
            



        
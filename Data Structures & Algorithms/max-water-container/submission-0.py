"""
understand:
- input: heights: array of ints, each int represents the height of a bar
- output: largest m such that m = (i2 - i1) * min(heights[i2] - heights[i1])

plan:
1. two pointers: 1 at beg, 1 at end
2. m = 0
3. while beg < end
4. diff = beg - end
5. p = diff * min(heights[beg], heights[end])
6. if p > m -> m = p
7. if heights[beg] == heights[end] -> beg +=1
8. elif heights[beg] > heights[end] -> end -=1
9. else -> beg +=1
10. return m
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        b, e = 0, len(heights) - 1
        m = 0
        while b < e:
            diff = e - b
            p = diff * min(heights[e], heights[b])
            if p > m:
                m = p
            
            if heights[b] == heights[e]:
                b +=1
            elif heights[b] > heights[e]:
                e -=1
            else:
                b +=1
                
        return m
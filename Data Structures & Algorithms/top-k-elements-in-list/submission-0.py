"""
Understand:
- inputs: nums (array of ints), k (int)
- output: k most frequent elements in array
Plan:
- for each num in array add its freq to a dict 
- make into new list where keys are sorted by values
- return lst[:k]
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
        lst = sorted(dct, key=dct.get, reverse=True)
        return lst[:k]
        
"""
Understand:
- inputs: nums(array of ints)
- output: len of longest sequence that can be made with nums.
          sequence: each num increases by 1 from prev

Plan:
- turn nums into a set to remove duplicates + o(1) search time for furture searches
- max_len_1 = 1
- max_len_e = 0
- min = min in the set
- while set is not empty
- remove min from the set
- if min += 1. if it's in set, increase max_len_1.
- if not, min = new min of set, 
- max_len_2 = max_len 1 if max_len 1 > max_len2, max_len 1 = 1 
return max(max_len_1, max_len_2)

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        max_1 = 1
        max_2 = 0
        mini = min(nums)
        while nums:
            nums.remove(mini)
            mini +=1
            if mini in nums:
                max_1 +=1
            elif nums:
                mini = min(nums)
                if max_1 > max_2:
                    max_2 = max_1
                max_1 = 1
            else:
                return max(max_1, max_2)
        
"""
Understand:
- inputs: nums (array of ints), target (int)
- output: i,j where nums[i] + nums[j] == target
- constraints: i can't == j.

Plan:
- make a seen dict
- for i, num in enumerate nums
- calculate diff (target - num)
- check if diff is in the seen dict. if so, return [i, seen[diff]]
- otherwise add num as a key and i the value in dict
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        
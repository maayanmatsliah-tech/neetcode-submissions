"""
Understand:
- inputs: nums (int array)
- output: bool rep. if any value appears 2+ times in nums

Plan:
- make an empty dict
- iterate through nums
- if num in seen return True
- else seen[num] = 1
- return False outside of for loop
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen: return True
            seen[num] = 1
        return False
        
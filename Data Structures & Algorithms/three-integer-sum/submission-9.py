'''
Understand:
- input: nums (array of ints)
- output: list of all 3 value combos such that their sum is 0 
           and all have dif positions

Plan:
1. sort nums
2. create empty list
3. make 3 pointers: 2 at the beginning of the list, and one that floats
While beg <= end
4. if pointers at the very end and beginning add to 0 and 0 is in the list, append and move pointers by 1
5. if pointer at beg + pointer at end > 0:
    - if beg pointer + beg pointer + 1 + end pointer =0  append to list, move beg and end pointer
    - otherwise move only end pointer by one
6. if pointer at beg + pointer at end < 0:
    - if beg pointer + end pointer + end pointer -1 = 0 append to list, move beg and end pointer
    - otherwise move only beg pointer by one
7. outside while loop, return lst
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = val + nums[l] + nums[r]
                if three_sum > 0:
                    r -=1
                elif three_sum < 0:
                    l +=1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l +=1
                    while nums[r] == nums[r+1] and l < r:
                        r -=1
        return res

                
                        
                           
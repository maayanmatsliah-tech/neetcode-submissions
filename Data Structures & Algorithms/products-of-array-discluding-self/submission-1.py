'''
understand:
- input: nums (array of ints)
- output: array where each index is the product of all
          elements of nums except the val at the curr index

plan:
- make prefix list:
    - make new empty list
    - original prefix = 1
    - i = 0
    - while i < len(nums)
    - push prefix to list
    - i +=1
    - prefix * nums[i]
- make suffix list:
    - original suffix = 1
    - i = len(nums) - 1
    - while i > -1
    - multiply lst[i] by suffix
    - i -=1
    - suffix * nums[i]
- return list

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        pre = 1
        i = 0
        while i < len(nums):
            lst.append(pre)
            i +=1
            pre *= nums[i - 1]
        post = 1
        i = len(nums) - 1
        while i > -1:
            lst[i] *= post
            i -=1
            post *= nums[i + 1]
        return lst
        

        
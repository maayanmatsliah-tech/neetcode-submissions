class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        while s <= e:
            m = ((e - s) // 2) + s
            mid = nums[m]
            if target < mid:
                e = m -1
            elif target > mid:
                s = m + 1
            else:
                return m
        return -1
        
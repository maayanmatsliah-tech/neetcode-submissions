"""
understand:
- inputs: s(str)
- output: bool repping if s is a palindrome
- palindrome: same fowards and backwards)

plan:
- left pointer is at first index of s, right at last
- while left <= right
- if s[left] !+ s[right] return false
- left +1, right - 1
- return True outside of loop
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [char.lower() for char in s if char.isalnum()]
        l, r = 0, len(lst) - 1

        while l <= r:
            if lst[l] != lst[r]:
                    return False
            l += 1
            r -= 1
        return True
        
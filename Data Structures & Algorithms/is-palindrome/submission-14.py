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
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            elif s[l].isalnum():
                r -=1
            else:
                l += 1
        return True
        
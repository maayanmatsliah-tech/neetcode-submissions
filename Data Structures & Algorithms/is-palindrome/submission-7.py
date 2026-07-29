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
        s_lst = [char.lower() for char in s if char.isalnum()]
        l = 0
        r = len(s_lst) - 1
        while l <= r:
            if s_lst[l] != s_lst[r]:
                return False
            l +=1
            r -=1
        return True
        
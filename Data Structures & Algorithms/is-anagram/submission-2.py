"""
Understand:
- inputs: s (str), t(str)
- output: bool rep. if s has all letter and same freqs. as t
Plan:
- create s dict and t dict, both empty
- iterate through chars of s and t, add them to dict where dict[char] = freq
- return s dict == t dict
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def helper(st):
            dct = {}
            for char in st:
                dct[char] = dct.get(char, 0) + 1
            return dct

        s_dct = helper(s)
        t_dct = helper(t)
        return s_dct == t_dct
        
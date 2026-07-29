"""
ENCODE:
    understand:
    - input: list of strs
    - output: one str where strs are combined. can add additional chars
    plan:
    - calc the length of each st. 
    - add it to a new str with a # after. then, the str.
    - do this for all strs
    - return s
ENCODE:
    understand:
    - input: one str consisting of multiple num, '#', and str sequences.
    - output: s sperated to original strs
    plan:
    - make a new list
    - make one pointers
    - make variable equal to empty string
    - while new str
    - set pointer = to the num at the begining + 2
    - append s[2:pointer]to the new list
    - new str = s[pointer:]
    - return list
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        new_s = ""
        for s in strs:
            new_s += f"{len(s)}#{s}"
        return new_s



    def decode(self, s: str) -> List[str]:
        new_lst = []
        i = 0
        j = i
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            content = s[j + 1: j + 1 + length]
            new_lst.append(content)
            i = j + 1 + length
        return new_lst

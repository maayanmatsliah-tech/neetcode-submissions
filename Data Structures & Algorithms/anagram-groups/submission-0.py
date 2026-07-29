"""
understand:
- input: list of strs
- output: lst[lst[str]] where each sub-list is created by grouping anagrams
plan:
- make each str into a dict where they key is an lst of the chars 
  sorted and the key is the og position in the list
- add to a new lst and sort by key
- make 2 pointers, where left is 0 and right is 1
- if new_lst[left] == new_lst[right], right +=1
- else append new_lst[left value in the dict]

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            sorted_str = "".join(sorted(word))
            if sorted_str in seen:
                seen[sorted_str].append(word)
            else:
                seen[sorted_str] = [word]
        return list(seen.values())

        
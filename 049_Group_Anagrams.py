'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        out_index = []
        for x in strs:
            one_set = dict()
            for y in x:
                if y not in one_set:
                    one_set[y] = 1
                else:
                    one_set[y] += 1
         
            if one_set in out:
                for tmp_idx, temp in enumerate(out):
                    if temp == one_set:
                        out_index[tmp_idx].append(x)
                
            else:
                out.append(one_set)
                out_index.append([])
                out_index[-1].append(x)
            
        return out_index

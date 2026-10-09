from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        ana_map = defaultdict(list)

        for s in strs:
            s_sorted = tuple(sorted(s))
            ana_map[s_sorted].append(s)

        for v in ana_map.values():
            res.append(v)

        return res
        


        
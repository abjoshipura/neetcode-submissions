from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each new string
        # -- compare its freq map with the freq maps of the groups
        # -- if any match, add it to the group
        # -- else, make a new group

        groups = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            groups[sorted_str].append(s)
            
        return list(groups.values())

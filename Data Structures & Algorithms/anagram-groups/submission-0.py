class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = dict()
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1

        flag = False
        for char in freq:
            flag = (flag or freq[char])

        return not flag

    # I make the code modular to determine if any two strings are anagrams of each other
    
    # When I see grouping, I immediately think of Kruskal's algorithm where you see the
    # use of Union and SetFind.

    # Here, if we think of each string as a node, then we don't really have edges, meaning
    # know exactly which nodes each string is from.

    # So, let's initialize each string into a group.
    # Compare one string from each group:
    # - If they are anagrams, merge the two groups
    # - If they are not anagrams, ignore.

    # Iterate over all groups such that we only have to compare to previous groups.

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupsDict = dict()

        for i in range(len(strs)):
            for string in strs[:i]:
                if self.isAnagram(strs[i], string):
                    groupsDict[string].append(strs[i])
                    break
            else:
                groupsDict[strs[i]] = [strs[i], ]
        
        return list(groupsDict.values())
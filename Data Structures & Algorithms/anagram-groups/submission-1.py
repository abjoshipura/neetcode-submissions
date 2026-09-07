from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            charArray = [0] * 26
            for char in string:
                charArray[ord(char) - 97] += 1
            
            anagrams[tuple(charArray)].append(string)
        
        return list(anagrams.values())
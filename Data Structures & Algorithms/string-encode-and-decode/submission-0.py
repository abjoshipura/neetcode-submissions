class Solution:
    def encode(self, strs: List[str]) -> str:
        sizes_str = ""
        words_str = ""

        for s in strs:
            sizes_str += str(len(s)) + ","
            words_str += s

        return sizes_str + "#" + words_str
    
    def decode(self, s: str) -> List[str]:
        hash_index = s.find("#")

        sizes_str = s[:hash_index]
        sizes = sizes_str.split(",")[:-1]

        strs = list()

        start = hash_index + 1
        for size in sizes:
            size = int(size)
            strs.append(s[start:start + size])
            
            start += size
        
        return strs
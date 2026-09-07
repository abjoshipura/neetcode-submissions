class Solution:
    def reverseBits(self, n: int) -> int:
        print(bin(n))
        return int(f"0b{bin(n)[2:][::-1].ljust(32, '0')}", 2)
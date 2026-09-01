class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     s = s.strip()
    #     n = len(s) -1
    #     # Time Complexity: O(n)
    #     # space Complexity : O(n) because of s.strip() which creates a new array copy in memory
    #     for i in range(n, -1, -1):
    #         if s[i] == ' ':
    #             return n - i
    #     return n

    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) -1
        # Time Complexity: O(n)
        # space Complexity : O(1) 
        while i >=0 and s[i] == ' ':
            i-=1
        
        length =0
        while i >=0 and s[i] != ' ':
            length += 1
            i-=1

        return length
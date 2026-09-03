class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     strs.sort(key=len)
    #     print(strs)
    #     prefix= strs[0]
    #     # Time Complexity: O(N log N + N * m) , where N log N  is of sorting and N*M is of loop
    #     # Space Complexity O(N) this is what internal sorting takes
    #     for word in strs[1:]:
    #         i=0
    #         while i < len(prefix):
    #             if prefix[i] != word[i]:
    #                 break
    #             i+=1
    #         prefix = prefix[:i]
    #     return prefix

     def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort() # sort lexicographically
        first= strs[0]
        last = strs[-1]
        prefix=""
        #  Time Complexity O(N log N * M) M is due to string to string comparison 
        # Space Complexity O(N)
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return prefix
            prefix+=first[i]
        
        return prefix

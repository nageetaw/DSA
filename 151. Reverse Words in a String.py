class Solution:
    def reverseWords(self, s: str) -> str:
        """ * **Time Complexity:** $O(N)$
        * **Space Complexity:** $O(N)$

        ### Breakdown
        * **`s.split()`:** Scans the entire string of length $N$ to separate words, taking $O(N)$ time and allocating $O(N)$ space for the resulting list of words.
        * **`s.reverse()`:** Reverses the list of words in-place, taking $O(K)$ time (where $K$ is the number of words) and $O(1)$ extra space.
        * **`" ".join(s)`:** Iterates through the words to build a new string, taking $O(N)$ time and allocating $O(N)$ space for the final output string. 
        """
        s = s.split()
        s.reverse()
        return " ".join(s)
    


        
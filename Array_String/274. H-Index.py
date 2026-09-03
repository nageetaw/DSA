class Solution:
    # def hIndex(self, citations: List[int]) -> int:
    #     """
    #     It Say atleast h paper that has atleast h citations and h should be maximum.
    #     Time Complexity: O(n^2)
    #     Space Complexity: O(1)
    #     """
    #     max_h =0
        
    #     # We iterate over paper, becuase 'h' can't be greater than total no of papers
    #     for h in range(1, len(citations)+1): 
    #         count = 0
    #         for i, citation in enumerate(citations):
    #             if citation >= h: # we increase count, if current paper has atleast h citations
    #                 count +=1
                
    #             if count == h: # if we found atleast 'h' citations 
    #                 max_h = max(max_h, h)
    #                 break
    #     return max_h


    def hIndex(self, citations: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Initialization
        n = len(citations) 
        counter =[]
        for i in range(n + 1): counter.append(0)

        # Each index in counter represents how many paper we have with that citations,
        # for the citations that exceed from length of paper we put those in last index(alteast)
        for citation in citations:
            if citation <= n:
                counter[citation] +=1
            else:
                counter[n] +=1
                
        papers, max_h = 0, 0
        
        for h in range(n, -1, -1):
            papers +=counter[h] # commulative the papers from backword becuase of atleast, so at current h, we can take all paper collectively that are after current h.
            if papers >= h: # atleast h paper with atleast h citations
                max_h= max(max_h, h)
        
        return max_h


        
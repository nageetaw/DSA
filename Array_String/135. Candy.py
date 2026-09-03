class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # The main learning from this question is:
        #  BREAK the question into two parts makes it easier to solve.
        # We did one pass to compare every child rating to it's left neighbour --> this make sure that every child has more candies than left neighbour
        # The second pass was to make sure that every child has more candies than thier right neighbour(We also make sure here to pick the max candies)
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(n - 2, -1 , -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i + 1] + 1, candies[i])

        return sum(candies)
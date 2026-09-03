class Solution:
    def jump(self, nums: List[int]) -> int:
        # Time Complexity: O(n) becuase even we have for loop inside while but that is toching each index only once since we are avoiding overlapping window already by setting the left pointer to right +1.
        # We are never visiting each index more than once hence it's O(n)
        # Space Complexity: O(1)
        # When we are at position 0, we have not made a jump
        total_jumps , left, right = 0 ,0, 0
        # --TIP: Consider left as near and right as far.
        while right < len(nums) - 1: 
            # We have to find how far we can reach being at current window (left -- right)
            max_reach = 0
            for i in range(left, right+1): #Find the max reach from current window
                max_reach = max(max_reach , nums[i] + i)
                    
            left = right +1
            right = max_reach
            total_jumps +=1 # we have jump once since we are traversing one window in every iteration.
        return total_jumps

        """
        It is not O(n^2) becuase In those cases, for an array of size n, the inner loop runs n times for each of the n outer iterations, resulting in n * n = n^2 operations.
        Here we never revisit a single element. 
        """
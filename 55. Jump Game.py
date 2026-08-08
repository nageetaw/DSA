class Solution:
    """
    The main lesson learned here:
    1- Don't always use while loop, if goal is to check if we reach at some point/goal use for loop
        this will save complicated if/else checks
    2- Think simple(This solution can be done using sliding window with two loops or DP as well)
    3- Think about greedy shortcuts
    """
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 

        # Goal is to reach last index, but if we can reach there from second last index, that means now we have 
        # to check can we reach at second last index from indexex before that, this we we update our Goal
        # ---Time complexity = O(n)
        # ---Space Complexity = O(1)
        
        # Work backwards from the second-to-last element down to 0th element
        # -- Using for lop simplyfy alot of conditions here for returning value
        for curr_idx in range(len(nums) - 2, -1, -1):
            # If the current index can reach or pass the current goal, 
            # shift the goal to this index
            if curr_idx + nums[curr_idx] >= goal:
                goal = curr_idx
                
        # If we successfully pushed the goal all the way back to the start (index 0)
        return goal == 0







class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water =0
        left, right= 0, n-1
        left_max , right_max = height[left], height[right]
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # The concept here is we will try to find the max on the left and right and then we will get the minimun of left and right and then subtract the current height to get the water i index can store.
        # The optimal solution finds the right max and left max on fly to get the water level each index can store based on the respective left or the right max.
        # We compare every time right max and left max to see which one is lower and then try to find the next higher one. and stops when both crosses each other.
        while left < right:
            if left_max >= right_max:
                right-=1
                right_max= max(right_max, height[right])
                water += right_max - height[right]
            else:
                left+=1
                left_max= max(left_max, height[left])
                water += left_max - height[left]

        return water
            
        
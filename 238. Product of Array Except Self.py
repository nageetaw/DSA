class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # SPACE Complexity: O(n)
        # TIME Complexity: O(n)
        n = len(nums)
        left, right = [1]*n ,[1]*n
        
        for i in range(1,len(nums)):
           right[i] = right[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            left[i] = left[i+1] * nums[i+1]

        for i in range(n):
            nums[i] = right[i]* left[i]
        
        return nums


        
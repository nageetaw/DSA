class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     if k > n:
    #         k = k % n 
    # if k > n the rotation gives same result is k includes multiple n.

    #     # Time complexity: O(n)
    #     # Space Complexity: O(n)
    #     split = n - k
    #     for i, num in enumerate (nums[split:] + nums[:split]):
    #         nums[i] = num


    # ----OPTIMIZED ---> The "Three-Step Reverse" Trick

    

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) # Space Complexity O(1)
        if k > n:
            k= k % n

        nums.reverse() # Step 1: rotate the list
        
        def reverse_portion(start, end):
            while start < end:
                nums[start], nums[end] = nums[end] , nums[start]
                start +=1
                end -=1
      
        reverse_portion(0, k-1) # step 2: rotate first k
        reverse_portion(k, n-1) # step 3: rotate last after k

    # We can also do the step 1 in the end.
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums) # Space Complexity O(1)
    #     if k > n:
    #         k= k % n

    #     def reverse_portion(start, end):
    #         while start < end:
    #             nums[start], nums[end] = nums[end] , nums[start]
    #             start +=1
    #             end -=1
      
    #     reverse_portion(n-k, n-1) # step 2: rotate first k
    #     reverse_portion(0, n-k-1) # step 3: rotate last after k
    #     nums.reverse() # Step 1: rotate the list


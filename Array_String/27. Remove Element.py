class Solution(object):

    # Refactored version
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i , j = 0, len(nums) -1
        # Why not O(n/2) every iteration moves either i forward or j backward — never both — so the loop runs at most n times total, not n/2 twice.
        # Time complexity O(n) 
        # Space O(1)
        while i <= j:
            if nums[i] == val: # when val = ith, replace and move j to left
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
            else: # else move i to right
                i+=1

        return i # return i since i points to the position where we have last value that is not equal to val.



    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i , j = 0, len(nums) -1
        # Time complexity O(n) 
        # Space O(1)
        while i <= j:
            if nums[j] == val: #if value is at j position move j to left
                j-=1

            if nums[i] != val: # if value is not at i position move i to right
                i+=1
            elif nums[i] == val and i < j: # if ith position has val, replace with jth position. but also make sure to replace only when i is less than j. 
                nums[i], nums[j] = nums[j], nums[i]

        return i # return i since i points to the position where we have last value that is not equal to val.
        
       
        
 
        
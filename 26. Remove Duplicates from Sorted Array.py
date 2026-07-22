class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <=1:
            return n
        
        i, j = 0, 1

        while j < n:
            if nums[i] != nums[j]:
                i+=1 # replace i+1 with j when ith != jth (both elements are not same, since j is always moving when elements are equal, so we have to find jth position when ith and jth are not equal and replace the next ith becuase we want one elemnet unique to be there. GOAL is to remove duplicates/)
                nums[i], nums[j] = nums[j], nums[i] 
            j+=1 # always move j to right
        return i+1
                
        
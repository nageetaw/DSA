class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     if n <=1:
    #         return n
        
    #     i, j = 0, 1

    #     while j < n::
    #         if nums[i] != nums[j]:
    #             i+=1 # replace i+1 with j when ith != jth (both elements are not same, since j is always moving when elements are equal, so we have to find jth position when ith and jth are not equal and replace the next ith becuase we want one elemnet unique to be there. GOAL is to remove duplicates/)
    #             nums[i], nums[j] = nums[j], nums[i] 
    #         j+=1 # always move j to right
    #     return i+1


    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i =0 

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
       
        return i+1
                
    #  Not much effiecinet for just unique number but will still work, good for keep at least k numbers and move others to end
    #  def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     j, count = 1, 1
    #     for i in range(1 , len(nums)):
    #         if nums[i] == nums[i-1]:
    #             count +=1
    #         else:
    #             count =1
            
    #         if count <=1:
    #             nums[j] = nums[i]
    #             j+=1
        
    #     return j
        
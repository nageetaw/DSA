class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     k = 2
    #     for i in range(2 , len(nums)):
    #         if nums[i] != nums[k-2]:
    #             nums[i], nums[k] = nums[k], nums[i]
    #             k+=1
        
    #     return k


    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j, count = 1, 1 # j is one that we update and i will scan the list
        for i in range(1 , len(nums)):
            if nums[i] == nums[i-1]: # if i and previous is same increase count
                count +=1
            else:
                count =1
            
            if count <=2: # since we have to keep at most 2, so update j 
                nums[j] = nums[i]
                j+=1
        
        return j
        

    # The below is to remove duplicates -- MEANS max a number will only appear once
    # In this since we init i =0 that is why we increament i before swapping
    #  it is the same pattern
    # plus the current pointer(the one in for loop) and swap and update the other one when current and other pointer elements are not equal.   

    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     i = 0 
    #     for j in range(1, len(nums)):
    #         if nums[i] != nums[j]:
    #             i+=1
    #             nums[i] = nums[j]
       
    #     return i+1
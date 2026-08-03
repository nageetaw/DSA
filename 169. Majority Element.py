from collections import Counter
class Solution(object):
    # def majorityElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #  Time complexity O(n) , space Complexity O(n)
    #     mapper = Counter(nums) # O(n)
    #     common = mapper.most_common(1)[0] # O(n)
    #     return common[0]


# --- CORE INTUITION --> THE TUG OF WAR GAME
# Boyer-Moore works by pairing up different elements and making them "cancel each other out."

# Imagine every time you see two different numbers, they fight and both are eliminated from the room.

# Because the majority element appears more than half the time, even if all the other numbers team up against it, the majority element will always survive at the end.
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Space complexity O(1)
        # Time Complexity O(N)
        count = 0
        elem = None

        for n in nums:
            # initially room is empty, so whoso ever comes takes the majority space
            if count == 0: 
                elem, count = n , count+1
                continue 
            # if room is not empty, and the same person comes, as majority, we increase count
            if n == elem:
                count +=1
            # else we decrease the count
            else:
                count -=1 
                
        return elem

        
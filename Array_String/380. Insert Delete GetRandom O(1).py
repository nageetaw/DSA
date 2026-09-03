import random
class RandomizedSet:
    # Time Complexity: O(1)
    # Space Complexity : O(n)
    def __init__(self):
        self._arr = []
        self._val_to_idx= {} # update this to value to idx map.
        
    def insert(self, val: int) -> bool:
        if val not in self._arr:
            self._val_to_idx[val] = len(self._arr) 
            self._arr.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self._arr:
            return False
        i = self._val_to_idx[val] # index where that element is
        last = len(self._arr) - 1 #last index of array
        if i < last :
            # swap the element with last index
            self._arr[i], self._arr[last] = self._arr[last] , self._arr[i]
            self._val_to_idx[self._arr[i]] = i #update the index of swapped last element
        self._arr.pop() # remove element from array
        del self._val_to_idx[val] # remove that element from set
        return True
        

    def getRandom(self) -> int:
        idx= random.randint(0, len(self._arr)-1)
        return self._arr[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
"""
LeetCode#380
Implement the RandomizedSet class:
RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. 
Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. 
Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""
import random

class RandomizedSet:
    def __init__(self):
       self.nums_list = []
       self.nums_dict = {}

    def insert(self, val):
        if val not in self.nums_dict:
            self.nums_dict[val] = len(self.nums_list)
            self.nums_list.append(val)
        return True
    
    def remove(self, val):
        if val in self.nums_dict:
            last_element, idx = self.nums_list[-1], self.nums_dict[val]
            self.nums_list[idx], self.nums_dict[last_element] = last_element, idx
            self.nums_list.pop()
            del self.nums_dict[val]
        return True
    
    def getRandom(self):
        return random.choice(self.nums_list)
    



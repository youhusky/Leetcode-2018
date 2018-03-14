#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
#
# algorithms
# Hard (29.52%)
# Total Accepted:    23.4K
# Total Submissions: 79.4K
# Testcase Example:  '["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n[[],[1],[1],[2],[],[1],[]]'
#
# Design a data structure that supports all following operations in average
# O(1) time.
# Note: Duplicate elements are allowed.
# 
# 
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The
# probability of each element being returned is linearly related to the number
# of same value the collection contains.
# 
# 
# 
# Example:
# 
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
# 
# // Inserts 1 to the collection. Returns true as the collection did not
# contain 1.
# collection.insert(1);
# 
# // Inserts another 1 to the collection. Returns false as the collection
# contained 1. Collection now contains [1,1].
# collection.insert(1);
# 
# // Inserts 2 to the collection, returns true. Collection now contains
# [1,1,2].
# collection.insert(2);
# 
# // getRandom should return 1 with the probability 2/3, and returns 2 with the
# probability 1/3.
# collection.getRandom();
# 
# // Removes 1 from the collection, returns true. Collection now contains
# [1,2].
# collection.remove(1);
# 
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();
# 
# 
#
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.dic = dict()

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val not in self.dic:
            self.dic[val] = set()
            self.dic[val].add(len(self.array))
            self.array.append(val)
            return True
        else:
            self.dic[val].add(len(self.array))
            self.array.append(val)
            
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        
        # val.index in self.array
        index = self.dic[val].pop()
        
        if index < len(self.array) - 1:
            
            last = self.array[-1]
            self.array[index] = last
            # last item delete
            # remove old insert new
            
            self.dic[last].remove(len(self.array)-1)
            self.dic[last].add(index)
            
        self.array.pop()
        if not self.dic[val]:
            del(self.dic[val])
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.array[random.randint(0, len(self.array)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

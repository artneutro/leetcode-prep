# https://leetcode.com/problems/insert-delete-getrandom-o1/
class RandomizedSet:

    import random

    def __init__(self):
        self.randomSet = {}

    def insert(self, val: int) -> bool:
        if val in self.randomSet :
            return False
        else :
            self.randomSet[val] = 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.randomSet :
            del self.randomSet[val]
            return True
        else :
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.randomSet.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


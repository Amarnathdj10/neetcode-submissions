class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap = {}

        if len(s) != len(t):
            return False

        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        
        for c in t:
            
            if hashmap.get(c, 0) == 0:
                return False
            
            hashmap[c] -= 1
        
        return True
        

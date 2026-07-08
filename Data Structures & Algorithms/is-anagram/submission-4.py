class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_table_s = {}
        hash_table_t = {}
        for char in s:
            hash_table_s[char] = hash_table_s.get(char,0)+1
        for char in t:
            hash_table_t[char] = hash_table_t.get(char,0)+1
        return hash_table_s == hash_table_t
        
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # sort both strings andcompare
        # O(nlog(n))
        if sorted(s) == sorted(t):
            return True
        else:
            return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Way 1
        # Just use the Counter function
        return Counter(s) == Counter(t)
        
        # Way 2
        # sort both strings andcompare
        # O(nlogn + mlogm)
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        # Way 2
        # 
        # if len(s) != len(t):
        #     return False

        # count_s, count_t = {}, {}



        
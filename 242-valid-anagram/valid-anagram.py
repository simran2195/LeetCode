class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Way 1
        # Just use the Counter function
        # O(n+m) time complexity
        # O(26)*2 space complexity
        # return Counter(s) == Counter(t)
        
        # Way 2
        # sort both strings andcompare
        # O(nlogn + mlogm)

        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        # Way 3
        # 
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)


        for ele in count_s:
            if count_s[ele] != count_t.get(ele, 0):
                return False
        
        return True


        
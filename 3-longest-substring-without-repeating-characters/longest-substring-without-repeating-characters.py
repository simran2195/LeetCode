class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        charSet = set()

        for r in range(len(s)):

            while s[r] in charSet:
                charSet.remove(s[l]) #if current char exists in set then remove the left index char add move left idx by 1
                l += 1


            charSet.add(s[r])
            res = max(res, r-l+1)
            
        return res

        
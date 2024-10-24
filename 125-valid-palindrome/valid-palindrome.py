class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        new_s = ""

        # remove all non-alnum chars
        for char in s:
            if char.isalnum():
                new_s += char

        # check for palindrome

        l, r = 0, len(new_s)-1

        while l < r:
            if new_s[l] == new_s[r]:
                l, r = l+1, r-1

            else:
                return False
        
        return True
    
        
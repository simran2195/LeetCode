class Solution:
    def isPalindrome(self, s: str) -> bool:

        # # to lower case
        # s = s.lower()

        # s_new = []
        # #ignore all non-alphanumeric characters
        # for c in s:
        #     if c.isalnum():
        #         s_new.append(c)

        # s_new = "".join(s_new)
        # return s_new[::-1] == s_new


        s_new = ""

        #ignore all non-alphanumeric characters
        for c in s:
            if self.isalnumcheck(c):
                s_new += c.lower()

        # using two pointers
        l, r = 0, len(s_new)-1

        while l < r:
            if s_new[l] == s_new[r]:
                l, r = l+1, r-1
            else:
                return False
        
        return True

    def isalnumcheck(self, c):
        if (ord(c) >= ord('0') and ord(c) <= ord('9')) or (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
            return True
        else:
            return False

    
        
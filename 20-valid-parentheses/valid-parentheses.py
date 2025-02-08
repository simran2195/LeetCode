# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:

        # Method 1: Brute force
        # O(n^2)
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

        return s == ""


        valid = {')' : '(',  '}' : '{', ']' : '['}
        stack = []

        # for char in s:
        #     if char in valid: # if there's a closing bracket, check for opening bracket
        #         if stack:
        #             top_element = stack.pop() 
        #         else:
        #             top_element = '#' # assign a dummy value

        #         if valid[char] != top_element:
        #             return False
                
        #     else:
        #         stack.append(char)

        # return not stack




    
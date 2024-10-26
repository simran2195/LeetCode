class Solution:
    def isValid(self, s: str) -> bool:

        valid = {')' : '(',  '}' : '{', ']' : '['}
        stack = []

        for char in s:
            if char in valid: # if there's a closing bracket, check for opening bracket
                if stack:
                    top_element = stack.pop() 
                else:
                    top_element = '#' # assign a dummy value

                if valid[char] != top_element:
                    return False
                
            else:
                stack.append(char)

        return not stack




    
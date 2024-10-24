class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        # Whitespace: Ignore any leading whitespace (" ").
        s = s.strip()

        # Edge case: If the string is empty after removing whitespace
        if not s:
            return 0

        # add correct sign to the string
        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]

        
            
        # check for leading zeros
        for l in range(len(s)):
            if s[l].isdigit() == False:
                break
            res = res * 10 + int(s[l])
                
            
            
        # Apply the sign
        res *= sign

        # Step 4: Clamp the result to the 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX


        return res
        


            



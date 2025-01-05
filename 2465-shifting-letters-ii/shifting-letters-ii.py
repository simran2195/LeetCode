# class Solution:
#     def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
#         s = list(s)
#         for row in shifts:
#             beg = row[0]
#             end = row[1]

#             # for forward shifts
#             if row[2] == 1: 
#                 for i in range(beg, end+1):
#                     if 'a' <= s[i] <= 'z':  # For lowercase letters
#                         s[i] = chr((ord(s[i]) - ord('a') + 1) % 26 + ord('a'))
                

#             # for backward shifts
#             elif row[2] == 0:
#                 for i in range(beg, end+1):
#                     if 'a' <= s[i] <= 'z':  # For lowercase letters
#                         s[i] = chr((ord(s[i]) - ord('a') - 1) % 26 + ord('a'))

#         s = "".join(s)
#         return s
        

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        delta = [0] * (n + 1)  # Difference array
        
        # Process the shifts into the difference array
        for start, end, direction in shifts:
            if direction == 1:
                delta[start] += 1
                delta[end + 1] -= 1
            else:
                delta[start] -= 1
                delta[end + 1] += 1
        
        # Accumulate the shifts to calculate the net shift for each character
        net_shifts = [0] * n
        shift = 0
        for i in range(n):
            shift += delta[i]
            net_shifts[i] = shift
        
        # Apply the shifts to the string
        result = []
        for i in range(n):
            # Calculate the new character after the net shift
            new_char = chr((ord(s[i]) - ord('a') + net_shifts[i]) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)


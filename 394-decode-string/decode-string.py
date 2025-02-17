class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            
            else:
                # pop from stack still we get "["
                seq = ""
                while stack[-1] != "[":
                    seq = stack.pop() + seq
                stack.pop() # remove the "["

                #  Now look for the freq
                freq = ""
                while stack and stack[-1].isdigit():
                    freq = stack.pop() + freq

                # append freq*seq to stack
                stack.append(int(freq)*seq)

        return "".join(stack)





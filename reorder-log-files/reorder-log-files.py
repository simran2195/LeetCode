# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        # Reorder these logs so that:

        # The letter-logs come before all digit-logs.
        # The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
        # The digit-logs maintain their relative ordering in original array. -> no need to sort

        digital_logs = []
        letter_logs = []

        # sorting the logs into digital or letter
        for log in logs:
            
            # check for digital or letter log
            # print("log = ", log)
            # just check the first character of the content
            content = log.split(" ")[1]
            # content = " ".join(content).replace(" ", "")
            # print(content)
            
            if content.isalpha():
                letter_logs.append(log)
            elif content.isdigit():
                digital_logs.append(log)

            letter_logs.sort(key = lambda x: (x.split(" ", 1)[1], x.split()[0]))
                

        
        return letter_logs + digital_logs



                
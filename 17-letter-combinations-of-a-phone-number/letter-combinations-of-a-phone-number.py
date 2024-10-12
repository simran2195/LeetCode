class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "prqs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backTrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]: # if digits[i] == 2, then c in "abc", 
                backTrack(i + 1, curStr + c)

        if digits:
            backTrack(0, "")

        return res





    
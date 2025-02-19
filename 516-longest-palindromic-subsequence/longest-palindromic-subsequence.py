class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1)+1)]

        # for i in range(len(text1)-1, -1, -1):
        #     for j in range(len(text2)-1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1+ dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                    
        # return dp[0][0]
        text1 = s
        text2 = s[::-1]
        N, M = len(text1), len(text2)
        dp = [[0] * (M+1) for _ in range(N+1)]

        for i in range(N):
            for j in range(M):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[N][M]
    

        
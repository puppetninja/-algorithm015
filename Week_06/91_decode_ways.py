class Solution:
    def numDecodings(self, s: str) -> int:
        codes = list(s)
        # Add empty string case
        dp = [0]*(len(codes)+1)
        # empty string has 1 way to decode
        dp[0] = 1
        dp[1] = 1 if codes[0] != '0' else 0
        for i in range(2, len(codes)+1):
            single = int(codes[i-1])
            combo = int(codes[i-2] + codes[i-1])
            if 1 <= single <= 9:
                dp[i] += dp[i-1]
            if 10 <= combo <= 26:
                dp[i] += dp[i-2]

        return dp[len(codes)]

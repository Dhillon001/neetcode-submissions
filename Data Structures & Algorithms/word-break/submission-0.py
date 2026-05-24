'''
U - understand 
    i - s and wordDict
    o - bolean (t/f)
    C - 1 <= s.length <= 200 and 1 <= wordDict.length <= 100
    E - 


P - Plan

'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i): 
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[n]       
        
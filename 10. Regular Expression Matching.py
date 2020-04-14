  def isMatch(s: str, p: str) -> bool:
      dp = [[False for _ in range(len(p) +1)] for _ in range(len(s) + 1)]
      dp[0][0] = True
      for j in range(len(p)):
          if p[j] == '*' and dp[0][j - 1]:
              dp[0][j+1] = True

      for i in range(len(s)):
          for j in range(len(p)):
              if s[i] == p[j] or p[j] == '.':
                  dp[i+1][j+1] = dp[i][j]
              elif p[j] == '*':
                  if s[i] != p[j-1] and p[j-1] != '.':
                      dp[i+1][j+1] = dp[i+1][j-1]
                  else:
                      dp[i+1][j+1]= dp[i+1][j-1] or dp[i][j+1] or dp[i+1][j] 
      return dp[-1][-1]

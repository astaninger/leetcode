def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    return self.helper(s, wordDict, {})
def helper(self, s, wordSet, memo):
    if s in memo: return memo[s]
    if not s: return ""
    result = []
    for word in wordSet:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            result += word,
        else:
          result += [word + " " + l for l in self.helper(s[len(word):], wordSet, memo)]
    memo[s] = result
    return result

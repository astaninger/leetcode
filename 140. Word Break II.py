def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    return helper(s, wordDict, {})
def helper(s, wordSet, memo):
    if s in memo: return memo[s]
    if not s: return ""
    result = []
    for word in wordSet:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            result += word,
        else:
          result += [word + " " + l for l in helper(s[len(word):], wordSet, memo)]
    memo[s] = result
    return result

import collections
def longestPalindrome(self, s: str) -> int:
    sc = collections.Counter(s)
    count = 0
    for i in sc:
        if sc[i] >= 2:
            count += (sc[i] // 2) * 2
    if count < len(s):
        count += 1
    return count 
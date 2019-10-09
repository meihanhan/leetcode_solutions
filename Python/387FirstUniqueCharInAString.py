import collections
def firstUniqChar(s: str):
    res = float('inf')
    dic = collections.Counter(s)
    for i in dic:
        if dic[i] == 1:
            res = min(res, s.find(i))
    if res >= len(s):
        return -1
    return res
def isAnagram(s: str, t: str):
    if len(s) != len(t):
        return False
    dic = {i: s.count(i) for i in set(s)}
    for key in dic:
        if key not in t or dic[key] != t.count(key):
            return False
    return True
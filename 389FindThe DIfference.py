def findTheDifference(s: str, t: str):
    dic = {x: s.count(x) for x in s}
    for i in t:
        if i not in dic.keys():
            return i
        if t.count(i) != dic[i]:
            return i
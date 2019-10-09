def uncommonFromSentences(A, B):
    res = {}
    result = []
    listA = A.split()
    listB = B.split()
    for i in listA:
        if i not in listB:
            if i not in res:
                res.update({i: 0})
            else:
                res[i] += 1
    for i in listB:
        if i not in listA:
            if i not in res:
                res.update({i: 0})
            else:
                res[i] += 1
    for i in res:
        if res[i] == 0:
            result.append(i)
    return result
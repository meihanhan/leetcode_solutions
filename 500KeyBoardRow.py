def findWords(words):
    rows = {'qwertyuiopQWERTYUIOP', 'asdfghjklASDFGHJKL', 'zxcvbnmZXCVBNM'}
    res = []
    for elem in words:
        for i in rows:
            if len(set(elem)) == len(set(i).intersection(set(elem))):
                res.append(elem)
    return res
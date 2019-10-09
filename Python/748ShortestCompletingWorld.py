def shortestCompletingWord(licensePlate, words):
    letters = []
    word = []
    for i in licensePlate:
        if 'A' <= i <= 'z':
            letters.append(i.lower())
    for i in words:
        temp = i
        checker = True
        for j in letters:
            if j in temp:
                temp = temp.replace(j, '', 1)
            else:
                checker = False
                break
        if checker:
            word.append(i)
    minLength = len(word[0])
    res = word[0]
    for i in word:
        if len(i) < minLength:
            res = i
            minLength = len(i)
    return res

shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"])
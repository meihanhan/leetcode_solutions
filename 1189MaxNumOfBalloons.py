def maxNumberOfBalloons(text):
    countChar = {'b': 0, 'a': 0, 'l': 0, 'n': 0, 'o': 0}
    for i in text:
        for key in countChar:
            if i == key:
                countChar[key] += 1
    if min(countChar):
        return min(min(countChar.values()), min(countChar['l'], countChar['o']) // 2)
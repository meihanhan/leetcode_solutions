def countCharacters(words, chars):
    res = 0
    for i in words:
        count = 0
        for j in i:
            if i.count(j) <= chars.count(j):
                count += 1
        if count == len(i):
            res += count
        print(count, res)
    print(res)
    return True

countCharacters(["cat",'bt','hat', "tree"], "atach")
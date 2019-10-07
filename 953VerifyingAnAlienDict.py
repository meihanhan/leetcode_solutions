def isAlienSorted(words,order):
    numList = []
    maxLength = 0
    for i in range(len(words)):
        maxLength = max(maxLength, len(words[i]))
        numList.append([])
        for j in words[i]:
            numList[i].append(order.index(j))
    print(numList)
    for i in range(maxLength):
        for j in range(len(numList) - 1):
            if len(numList[j]) < maxLength:
                for x in range(maxLength - len(numList[j])):
                    numList[j].append(0)
            print(i, j, numList[j])


            if numList[j][i] > numList[j + 1][i]:
                print(numList[j][i], numList[j+1][i])
                return False
            if numList[j][i] < numList[j + 1][i]:
                print(numList[j][i], numList[j+1][i], i, j)
                break
        else:
            continue
    return True

isAlienSorted(["hello","leetcode","abc"], "hlabcdefgijkmnopqrstuvwxyz")
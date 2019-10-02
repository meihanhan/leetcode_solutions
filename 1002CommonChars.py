def commonChars(A):
    myList = []
    minStr = A[0]
    for i in A:
        if len(i) < len(minStr):
            minStr = i
    temp = minStr
    for elem in A:
        ans = ''
        for i in elem:
            if i in temp:
                temp = temp.replace(i, '', 1)
                ans += i
        myList.append(ans)
        temp = min(myList, key=len)
    return temp

commonChars(["cool","lock","cook"])
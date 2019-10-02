def commonChars(A):
    ans = ''
    minStr = A[0]
    for i in A:
        if len(i) < len(minStr):
            minStr = i
    temp = minStr
    for elem in A:
        counter = 0
        for i in elem:
            if i in temp:
                temp = temp.replace('i', '0')
                ans += i
        temp = ans
    return ans

commonChars(["bella","label","roller"])
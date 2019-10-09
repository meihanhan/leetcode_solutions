def isHappy(n):
    sums = []

    while n != 1:
        temp = 0
        for i in str(n):
            temp += int(i) * int(i)
        if temp in sums:
            return False
        sums.append(temp)
        n = temp
    return True
def findRestaurant(list1, list2):
    d1 = {x: list1.index(x) for x in list1}
    d2 = {x: list2.index(x) for x in list2}
    res = [2000, []]
    for i in d1:
        if i in d2:
            if res[0] == d1[i] + d2[i]:
                res[1].append(i)
            if res[0] > d1[i] + d2[i]:
                res[0] = d1[i] + d2[i]
                res[1] = [i]

    return res[1] 
def subdomainVisits(cpdomains):
    dic = {}
    for elem in cpdomains:
        print(dic)
        fullDomain = elem.split(' ')[1]
        visitCount = int(elem.split(' ')[0])
        if fullDomain in dic:
            dic[fullDomain] += visitCount
        else:
            dic.update({fullDomain: visitCount})
        subDomain = fullDomain
        while subDomain.count('.') > 0:
            subDomain = subDomain.split('.', 1)[1]
            print(subDomain)
            if subDomain in dic:
                print(dic[subDomain], visitCount, elem)
                dic[subDomain] += visitCount
            else:
                dic.update({subDomain: visitCount})
    res = []
    for key, value in dic.items():
        res.append(str(value) + " " + key)
    print(res)
    return res
subdomainVisits(["100 c.b.a", "50 b.a", "1 d.a", "5 A"])
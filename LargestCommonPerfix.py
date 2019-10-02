def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    shortStr = strs[0]
    for elem in strs:
        if len(elem) < len(shortStr):
            shortStr = elem
    perfix = ''
    for i in range(len(shortStr)):
        for elem in strs:
            if elem[i] != shortStr[i]:
                return perfix
        perfix += shortStr[i]
    return perfix
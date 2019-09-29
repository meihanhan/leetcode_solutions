def romanToInt(s: str):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    passIt = False
    for i in range(len(s)):
        if passIt:
            passIt = False
            continue
        if (i + 1 < len(s)) and (symbols[s[i]] < symbols[s[i + 1]]):
            result += symbols[s[i + 1]] - symbols[s[i]]
            passIt = True
        else:
            result += symbols[s[i]]
    return result

romanToInt('MCMXCIV')
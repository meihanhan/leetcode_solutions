def findOcurrences(text: str, first: str, second: str):
    res = []
    splitText = text.split()
    for i in range(len(splitText) - 2):
        if splitText[i] == (first):
            if splitText[i + 1] == (second):
                res.append(splitText[i + 2])
                i += 2

    return res
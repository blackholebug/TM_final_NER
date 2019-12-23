def prefix1(words):
    result = []
    for word in words:
        temp = word[:1]
        result.append(temp)
    return result

def prefix2(words):
    result = []
    for word in words:
        temp = word[:2]
        result.append(temp)
    return result

def prefix3(words):
    result = []
    for word in words:
        temp = word[:3]
        result.append(temp)
    return result

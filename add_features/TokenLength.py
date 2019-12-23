def tokenlen(words):
    result = []
    for word in words:
        length = len(word)
        result.append(str(length))
    return result
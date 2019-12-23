def part2word(words):
    result = []
    for word in words:
        temp = word[-2:]
        result.append(temp)
    return result

def part3word(words):
    result = []
    for word in words:
        temp = word[-3:]
        result.append(temp)
    return result

def part4word(words):
    result = []
    for word in words:
        temp = word[-4:]
        result.append(temp)
    return result

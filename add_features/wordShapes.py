import string
punc = string.punctuation

def wordShapes(words):
    result = []
    for word in words:
        for char in word:
            if char.isupper():
                word = word.replace(char, 'X')
            elif char.islower():
                word = word.replace(char, 'x')
            elif char.isdigit():
                word = word.replace(char, 'd')
            elif char in punc:
                pass
            else:
                pass
        result.append(word)
    return result

def isallpunc(word):
    for char in word:
        if char not in punc:
            return False
    return True

def shapetype(words):
    result = []
    for word in words:
        if(word.isupper()):
            result.append("isupper")
        elif(word.istitle()):
            result.append("istitle")
        elif(isallpunc(word)):
            result.append("isallpunc")
        elif(word.isdigit()):
            result.append("isdigit")
        else:
            result.append("null")
    return result

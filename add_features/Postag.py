import nltk
def postag(words):
    pos_tags = nltk.pos_tag(words)
    result = []
    for (word,tag) in pos_tags:
        result.append(tag)
    return result

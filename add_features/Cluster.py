dic = {}
with open("cluster_path",'r') as fin:
    for line in fin.readlines():
        line = line.strip()
        arr  = line.split("\t")
        word = arr[1]
        cls = arr[0]
        dic[word] = cls

def add_cluster(words):
    result = []
    for word in words:
        if(word in dic):
            result.append(dic[word])
        else:
            result.append("NULL")
    return result

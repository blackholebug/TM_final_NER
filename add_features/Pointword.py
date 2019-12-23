dic={}
with open("point_word.txt",'r') as fin:
    for line in fin.readlines():
        line = line.strip()
        arr = line.split("\t")
        dic[arr[0]] = arr[1]

def Pointword(words):
    result=["NULL" for i in range(len(words))]
    i = 0 
    while(i < len(words)):
        # reverse the list
        for j in range(i,len(words))[::-1]:
            plat_str = " ".join(words[i:j+1]).lower()
            if(plat_str in dic):
                for k in range(i,j+1):
                    # result[k] = "Gazetteer"
                    if(k==i):
                        result[k] = dic[plat_str]
                    else:
                        result[k] = dic[plat_str]
                i = j 
                break
        i+=1
    return result

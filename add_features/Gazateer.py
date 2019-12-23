import re
myDictionary = {}
with open("../lexicon/gazateer.dict",'r', encoding='utf-8') as fin:
    for line in fin.readlines():
        line = line.strip()
        arr = line.split("\t")
        if(len(arr)!=2):
            continue
        myDictionary[arr[0]] = arr[1].lower()

def get_gazateer(words):
    result=["NULL" for i in range(len(words))]
    i = 0
    while(i < len(words)):
        # reverse the list
        for j in range(i,len(words))[::-1]:
            plat_str = " ".join(words[i:j+1]).lower()
            if(plat_str in myDictionary):
                for k in range(i,j+1):
                    # result[k] = "Gazetteer"
                    if(k==i):
                        result[k] = "B-"+myDictionary[plat_str]
                    else:
                        result[k] = "I-"+myDictionary[plat_str]
                i = j
                break
        i+=1
    return result       

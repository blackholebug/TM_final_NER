import os
import re
p_dot = re.compile("\.")
path = "./raw"
filelist = os.listdir(path)
whole_dic = {}
for filename in filelist:
    with open(os.path.join(path,filename),'r',encoding='utf-8') as fin:
        tag = p_dot.sub("_",filename)    
        for line in fin.readlines():
            line = line.strip()
            if(line in whole_dic):
                whole_dic[line].append(tag)
            else:
                whole_dic[line]=[tag]

with open("gazateer.dict",'w',encoding='utf-8') as fg,open("repeated",'w',encoding='utf-8') as fr:
    for it in whole_dic:
        tagset = set(whole_dic[it])
        fg.write(it+"\t"+list(tagset)[0]+"\n")
        if(len(tagset)!=1):
            fr.write(it+"\t"+" ".join(list(tagset))+"\n")
    

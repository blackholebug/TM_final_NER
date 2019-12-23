import os,sys
import ShapeModify,Postag
import wordShapes
import Gazateer
import Partofword
import TokenLength
import Cluster
import Prefix
import Pointword


class sentence_obj():
    def __init__(self, lines):
        self.feature_dic = {}
        self.words = []
        self.tags = []
        for l in lines:
            arr = l.split("\t")
            self.words.append(arr[0])
            self.tags.append(arr[1])
    
    def print_sentence(self, feature_names, fout):
        for i,word in enumerate(self.words):
            temp = []
            temp.append(word)
            for name in feature_names:
                if(name not in self.feature_dic):
                    temp.append("NULL")
                else:
                    temp.append(self.feature_dic[name][i])
            temp.append(self.tags[i])
            fout.write("\t".join(temp)+"\n")
        fout.write("\n")
    
    def add_feature(self, feature_name , feature_arr):
        try:
            assert len(feature_arr)==len(self.words)
        except:
            print(feature_arr,self.words)
            exit()
        self.feature_dic[feature_name] = feature_arr

def read_data(filepath):
    result = []
    buf = []
    with open(filepath,'r',encoding='utf-8') as fin:
        for line in fin.readlines():
            line = line.strip()
            if(line==""):
                if(len(buf)!=0):
                    result.append(buf)
                    buf = []
                continue
            buf.append(line)
        if(len(buf)!=0):
            result.append(buf)
    return result

def produce_data(rawdata, feature_names, fout):
    for sent in rawdata:
        if(len(sent)==""):
            continue
        sent_obj = sentence_obj(sent)
        #################################################
        #####add your feature below######################
        #################################################

        #add lower shape below#
        lowershapes = ShapeModify.lowermaker(sent_obj.words)
        sent_obj.add_feature("lower",lowershapes)
        #add postag below#
        postags = Postag.postag(sent_obj.words)
        sent_obj.add_feature("postag",postags)
        #add wordshape below#
        wordshapes = wordShapes.wordShapes(sent_obj.words)
        sent_obj.add_feature("wordshapes", wordshapes)
        #add gazateer below#
        gazateer = Gazateer.get_gazateer(sent_obj.words)
        sent_obj.add_feature("gazateer", gazateer)
        #add wordshpetype below#
        allcaptial = wordShapes.shapetype(sent_obj.words)
        sent_obj.add_feature("wordshapetype", allcaptial)
        #add part of word below#
        part4word = Partofword.part4word(sent_obj.words)
        sent_obj.add_feature("part4word", part4word)
        # add part of word below#
        part3word = Partofword.part3word(sent_obj.words)
        sent_obj.add_feature("part3word", part3word)
        # add part of word below#
        part2word = Partofword.part2word(sent_obj.words)
        sent_obj.add_feature("part2word", part2word)
        # add length of token below#
        tokenlen = TokenLength.tokenlen(sent_obj.words)
        sent_obj.add_feature("tokenlen", tokenlen)
        #cluster feature add below#
        cluster_feature = Cluster.add_cluster(sent_obj.words)
        sent_obj.add_feature("cluster_path", cluster_feature)
        #add prefix below#
        prefix1 = Prefix.prefix1(sent_obj.words)
        sent_obj.add_feature("prefix1", prefix1)
        prefix2 = Prefix.prefix2(sent_obj.words)
        sent_obj.add_feature("prefix2", prefix2)
        prefix3 = Prefix.prefix3(sent_obj.words)
        sent_obj.add_feature("prefix3", prefix3)
		#add point to word#
        pointword = Pointword.Pointword(sent_obj.words)
        sent_obj.add_feature("pointword", pointword) 
        #################################################
        sent_obj.print_sentence(feature_names, fout)

if __name__ == '__main__':
    feature_names = ["lower","postag","wordshapes","gazateer","wordshapetype",
                     "part4word","part3word","part2word","tokenlen",
                     "prefix1","prefix2","prefix3","cluster_path","pointword"]
    train_set = read_data("../rawdata/train")
    train_set += read_data("../rawdata/dev")
    test_set = read_data("../rawdata/test")
    
    train_notypes_set = read_data("../rawdata/train_notypes")
    train_notypes_set += read_data("../rawdata/dev_notypes")
    test_notypes_set = read_data("../rawdata/test_notypes")

    with open("../train.data",'w', encoding='utf-8') as fout:
        produce_data(train_set,feature_names,fout)
    with open("../test.data",'w', encoding='utf-8') as fout:
        produce_data(test_set,feature_names,fout)
    with open("../train_notypes.data",'w', encoding='utf-8') as fout:
        produce_data(train_notypes_set,feature_names,fout)
    with open("../test_notypes.data",'w', encoding='utf-8') as fout:
        produce_data(test_notypes_set,feature_names,fout)

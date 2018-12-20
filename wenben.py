#文本挖掘
import jieba
import jieba.posseg #得词性
sentence="我喜欢微积分，高效能，好用"
w1=jieba.cut(sentence,cut_all=True) #第一个参数为要分词的内容，第二个代表模式，设置为全模式
for item in w1:#通过循环输出
    print(item) #会有叠加
print(" ")
w2=jieba.cut(sentence,cut_all=False)#模式为精准模式,省略模式，默认为精准模式
for item in w2:
    print(item)
print("")
w3=jieba.cut_for_search(sentence)#搜索引擎模式
for item in w3:
    print(item)
#得到词性
w5=jieba.posseg.cut(sentence)
#用.flag调用词性，.word调用词语
#r代词t时间u助词v动词vn名动词w标点符号un未知词语
# p:介词nz:其他专有名词，a:形容词，c:；连词，d:副词，
# e:叹词，f:方位词i:成语，m:数词，n:名词，nr:人名，nt:机构团体，ns:地名
for item in w5:
    print(item.word+"---"+item.flag)
#词典加载
#jieba.load_userdict("D:\dict3.txt")#可以在同一文件夹中加入自定义的词
#更改词频（两中）
sentence="最优化理论很重要"
w7=jieba.cut(sentence)
for item in w7:
    print(item)
print("")
#jieba.add_word("很重要")#将其做为一个词语，添加进入词典
jieba.suggest_freq("很重要",True)#改词频
w8=jieba.cut(sentence)
for item in w8:
    print(item)
#提取文本中的关键词
import jieba.analyse
sentence3="阳光灿烂，生活很美好,奋斗不停"
tag=jieba.analyse.extract_tags(sentence3,4)
print(tag)
#返回词语的位置
w9=jieba.tokenize(sentence)
for item in w9:
    print(item)
print("")
#文心雕龙的关键词提取
data=open("文心雕龙.txt","r",encoding='utf-8').read()
tag=jieba.analyse.extract_tags(data,20)
print(tag)



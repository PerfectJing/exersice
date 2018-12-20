#文本相似性分析
from gensim import corpora,models,similarities
import jieba
from collections import defaultdict
#1读取文档
doc1="文心雕龙.txt"
d1=open(doc1,"r",encoding='utf-8').read()

#2进行分词
data1=jieba.cut(d1)
#3将文档中的词间隔空格，便于计算
data11=""
for item in data1:
    data11+=item+" "
    #print(data11)
documents=[data11]
texts=[[word for word in document.split()]
       for document in documents]
from collections import defaultdict
#4计算词频
#如果访问字典中不存在的键，会引发KeyError异常,defaultdict的作用是在于，
# 当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值，
frequency=defaultdict(int)#defaultdict接受一个工厂函数作为参数,int=0
for text in texts:
    for token in text:
        frequency[token]+=1
#5对出现频率低的词过滤掉，如小于3的
texts=[[word for word in text if frequency[token]>3]
       for text in texts]
#6建立词典,并使用save函数将词典保存
dictionary=corpora.Dictionary(texts)
#字典有很多功能
# diction.token2id 存放的是单词-id key-value对
# diction.dfs 存放的是单词的出现频率
dictionary.save("wsimiliar.txt")
#7加载要对比的文档
doc2="写作这回事(恐怖小说之王的人生回忆录)Txt-[美]斯蒂芬金.txt"
d2=open(doc2,"r",encoding='gbk').read()#编码
data2=jieba.cut(d2)
data21=""
for item in data2:
    data21+=item+" "
    #print(data31)
new_doc=data21
#8.将要对比的文档通过doc2ow转化为稀疏向量
new_vec=dictionary.doc2bow(new_doc.split())#有空格，切割一下
#9.进一步处理，得到新语料库
corpus=[dictionary.doc2bow(text) for text in texts]
tfidf=models.TfidfModel(corpus)#将文档由按照词频表示 转变为按照tf-idf格式表示
#10.通过token2id得到特征数
featureNum=len(dictionary.token2id.keys())
#11.计算稀疏矩阵的相似度，建立索引
index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)
simlarity=index[tfidf[new_vec]]
print(simlarity)

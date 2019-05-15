import requests
import json
from sklearn.feature_extraction.text import CountVectorizer
import pymysql
from snownlp import SnowNLP
from imageio import imread
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import PIL.Image as Image

def get_data():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user='root', passwd="ljc123", port=3306, db="weibo_cxk")

    # 使用cursor()方法获取操作游标


    cursor = db.cursor()
    print(cursor)
    sql = 'SELECT word FROM wyf_repost WHERE id < 10000'
    cursor.execute(sql)
    res = cursor.fetchall()

    # print(res)
    return res

# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    # 让飞只显示一次。
    jieba.suggest_freq("吴亦凡", True)
    jieba.load_userdict('protectdict.txt')  # filename为自定义词典的路径
    sentence_seged = jieba.cut_for_search(sentence.strip())
    stopwords = stopwordslist('chineseStopWords.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


def deal_data():
    wordlist = []

    res = get_data()
    for i in res:
        signature = str(i).strip().replace('/@', '').replace('(','').replace(')','').replace("'",'').replace(',','').replace('#','').replace(' ','').replace('[','').replace(']','')
        rep = re.compile('1f\d+\w*|[<>/=]')
        signature = rep.sub('', signature)
        wordlist.append(signature)
    # print(wordlist)
    text = ''.join(wordlist)
    print(text)
    return text
    #
    # silist = jieba.cut(text, cut_all=False)
    # word_space_split = " ".join(silist)
    # print(word_space_split)

def feel_any(list):
    sentimentslist = []
    for i in list:
        s = SnowNLP(i)
        # print s.sentiments
        sentimentslist.append(s.sentiments)
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('Analysis of Sentiments')
    plt.show()

def mk_wc(text):
    # 设置词云
    stopws = ['微博','xa0','转发','u200b']
    wc = WordCloud(background_color="white",  # 设置背景颜色
                   mask=imread('cxk5.png'),  # 设置背景图片
                   scale=8,  # 清晰度
                   max_words=2000,  # 设置最大显示的字数
                   prefer_horizontal=.5,
                   stopwords=stopws,  # 设置停用词
                   font_path="C:\Windows\Fonts\STXIHEI.TTF",  # 设置为楷体 常规
                   # 设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
                   max_font_size=60,  # 设置字体最大值
                   random_state=20,  # 设置有多少种随机生成状态，即有多少种配色方案
                   relative_scaling=0.8, #"float：默认值'auto'，文字出现的频率与字体大小的关系，设置为1时词语出现的频率越高，其字体越大，默认为0.5。
                   width=700,
                   height=500,
                   )
    myword = wc.generate(text)  # 生成词云
    wc.to_file('wyf.jpg')
    return myword


# 词袋词频向量化
def word_bag():

    vectorizer = CountVectorizer()
    corpus = ["I come to China to travel",
              "This is a car polupar in China",
              "I love tea and Apple ",
              "The work is to write some papers in science"]
    # print(vectorizer.fit_transform(corpus))
    print(vectorizer.fit_transform(corpus).toarray())
    print(vectorizer.get_feature_names())



def tf_tdf():
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf2 = TfidfVectorizer()
    corpus = ["I come to China to travel",
              "This is a car polupar in China",
              "I love tea and Apple ",
              "The work is to write some papers in science"]
    re = tfidf2.fit_transform(corpus)
    print(re)

# 高频词
def text_rank():
    from jieba import analyse
    textrank = analyse.textrank
    text = deal_data()

    # 基于TextRank算法进行关键词抽取
    keywords = textrank(text)
    # 输出抽取出的关键词
    for keyword in keywords:
        print(keyword + "/")

# 词频统计、降序排序
def text_times():
    text = deal_data()
    words = jieba.cut_for_search(text)
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    freq_word = []
    for word, freq in word_freq.items():
        freq_word.append((word, freq))
    freq_word.sort(key=lambda x: x[1], reverse=True)  # 反序排列，根据第二个参数
    max_number = int(input(u"需要前多少位高频词？ "))
    for word, freq in freq_word[: max_number]:
        print(word, freq)



if __name__ == '__main__':
    # 分词
    # text = seg_sentence(deal_data())
    # print(text)

    # 生成词云
    # myword = mk_wc(text)

    # 展示词云图
    # plt.imshow(myword)
    # plt.axis("off")
    # plt.show()

    # 情感分析
    # feel_any(text)
    # tf_tdf()

    #提取关键词
    # text_rank()

    # 高频词
    text_times()
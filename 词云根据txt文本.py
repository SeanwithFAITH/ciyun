#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/04/23 21:26
# @Author  : SEAN_ZHOU (${email})
# @Link    : ${link}
# @Version : $Id$
# @Title：

import numpy as np
from PIL import Image
import re
import jieba
from wordcloud import WordCloud,ImageColorGenerator#,STOPWORDS
import  matplotlib.pyplot as plt

# 打开存放项目名称的txt文件
with open(r'.\源文本\01.txt','r',encoding='utf-8-sig') as f:
    word= (f.read())
    f.close()

# 图片模板和字体
image=np.array(Image.open('03.png')) 
# font=r'.\字体\简体站酷文艺.ttf' 
font=r'.\字体\繁体思源宋.otf' 

# 去掉英文，保留中文 
resultword=re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\。\@\#\\\&\*\%]", "",word) 
wordlist_after_jieba = jieba.cut(resultword) 
wl_space_split = " ".join(wordlist_after_jieba) 

# 设置停用词
def read_word(file):
    temp=[w.decode('utf-8') for w in file.read().strip().split()]
    print(type(temp[0]))#查看类型
    temp[0]=''.join(temp[0].split('\ufeff'))#''一个空字符
    #print(temp)
    return temp

swfile=open("stopwords_CN.txt",'rb')
sw=read_word(swfile)
sw.append("\n")  # 停用词中增加换行符
sw.append(" ")   
# sw = set(STOPWORDS) 
# sw.add("研发")
# sw.add("系列")
# sw.add("这里不多写了，根据自己情况添加")

# 关键一步
my_wordcloud = WordCloud(scale=4,font_path=font,mask=image,stopwords=sw,background_color='white',
                         max_words = 100,max_font_size = 120,random_state=20).generate(wl_space_split) 

#显示生成的词云 
plt.imshow(my_wordcloud)
plt.axis("off") 
plt.show() 

#保存生成的图片
my_wordcloud.to_file('result.jpg')
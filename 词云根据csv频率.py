#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/04/23 21:26
# @Author  : SEAN_ZHOU (${email})
# @Link    : ${link}
# @Version : $Id$
# @Title：

import numpy as np
import pandas as pd
from PIL import Image
import re
import jieba
from wordcloud import WordCloud,ImageColorGenerator#,STOPWORDS
import  matplotlib.pyplot as plt
from pathlib import Path

currentPath = Path(".")#当前位置
# 设置这里的字体和源文本文件
pathOfFont = currentPath / "字体" / "sy.otf"
pathOfText = currentPath / "源文本" / "琉璃.csv"
font = str(pathOfFont)
yuanfile = str(pathOfText)
image=np.array(Image.open('形状.png')) # 管形状,注意图片要处理成白底黑型
bi_c = np.array(Image.open('颜色.jpg')) # 管颜色（高度要比上面那个大）
img_colors = ImageColorGenerator(bi_c)
stop_words = open("stopwords_CN.txt",encoding="utf8").read().split("\n")
# 读取词频文件
# fp = pd.read_csv(yuanfile, encoding='utf-8')
fp = pd.read_csv(yuanfile)
name = list(fp.word)  # 词
value = fp.val  # 词的频率
for i in range(len(name)):
    name[i] = str(name[i])
dic = dict(zip(name, value))  # 词频以字典形式存储



# 关键一步
my_wordcloud = WordCloud(scale=4,font_path=font,mask=image,mode='RGBA',background_color=None,
                         max_words = 800,max_font_size = 90,random_state=,stopwords=stop_words,color_func=img_colors)
my_wordcloud.generate_from_frequencies(dic)
#显示生成的词云 
plt.imshow(my_wordcloud)
plt.axis("off") 
plt.show() 

#保存生成的图片
my_wordcloud.to_file('result2.png')
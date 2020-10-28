#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/04/23 21:08
# @Author  : SEAN_ZHOU (${email})
# @Link    : ${link}
# @Version : $Id$
# @Title：

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
 
# 打开文本
text = open('01.txt',encoding='utf-8-sig').read()
 
# 中文分词
text = ' '.join(jieba.cut(text))
print(text[:100])
 
# 生成对象
wc = WordCloud(font_path='简体站酷文艺.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)
# wc = WordCloud(font_path='繁体思源宋.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)
 
# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
 
# 保存到文件
wc.to_file('wordcloud3.png')
# ————————————————
# 版权声明：本文为CSDN博主「天痕坤」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/kun1280437633/article/details/89474284
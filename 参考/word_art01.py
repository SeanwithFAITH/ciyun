#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/04/17 15:38
# @Author  : SEAN_ZHOU (${email})
# @Link    : ${link}
# @Version : $1.0$
# wordart

from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
# 打开文件
text = open('01.txt',encoding='utf-8-sig').read()
 
# 生成对象
wc = WordCloud().generate(text=text)
print(type(wc))
# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
 
# 保存文件
wc.to_file('wordcloud.png')

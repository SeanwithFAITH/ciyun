#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/04/23 22:05
# @Author  : SEAN_ZHOU (${email})
# @Link    : ${link}
# @Version : $Id$
# @Title：

import numpy as np
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image


def draw_cloud(read_name):
    image = Image.open('china_map.jpg')  # 作为背景轮廓图
    graph = np.array(image)
    # 参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状
    wc = WordCloud(font_path='simkai.ttf', background_color='black', max_words=100, mask=graph)
    fp = pd.read_csv(read_name, encoding='gbk')  # 读取词频文件, 因为要显示中文，故编码为gbk
    name = list(fp.name)  # 词
    value = fp.val  # 词的频率
    for i in range(len(name)):
        name[i] = str(name[i])
    dic = dict(zip(name, value))  # 词频以字典形式存储
    wc.generate_from_frequencies(dic)  # 根据给定词频生成词云
    image_color = ImageColorGenerator(graph)
    plt.imshow(wc)
    plt.axis("off")  # 不显示坐标轴
    plt.show()
    wc.to_file('nsfc依托单位词云.png')  # 图片命名


if __name__ == '__main__':
    draw_cloud("support_institution.csv")
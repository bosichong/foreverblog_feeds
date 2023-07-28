import re

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

titles = []
stopwords = ['的', '是', '和', '在', '有', '我', '你', '他', '她', '它',]

# 打开文件
with open('titles.txt', 'r', encoding='utf-8') as f:
    for line in f:
        titles.append(line)

words = []
for title in titles:
    text = re.sub('\W*', '', title)
    words.extend(jieba.cut(text,cut_all=True))

word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1

sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

filtered_data = [(word, freq) for word, freq in sorted_word_counts if len(word) > 1]


# 只展示词语出现最多的前200个
top_200_words = filtered_data[:200]
# print(top_200_words)

font_path ='msyh.ttc'
# 创建WordCloud对象，并根据词频数据生成词云图
wordcloud = WordCloud(width=1920, height=1080,font_path=font_path, background_color="white").generate_from_frequencies(dict(top_200_words))

# 绘制词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # 不显示坐标轴
plt.show()
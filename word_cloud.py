# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud
import matplotlib.pyplot as plt

words = []

with open('db.txt', 'r', encoding='utf-8') as File:
    for line in File:
        if len(line) > 3:
            words.append(str(line))

wordcloud = WordCloud(
    width=400,
    height=400,
    background_color='black',
    min_font_size=10).generate(' '.join([item for item in words]))

# plot the WordCloud image
plt.figure(figsize=(24, 24), facecolor=None)
plt.imshow(wordcloud)
plt.axis("on")
plt.tight_layout(pad=0)
plt.show()

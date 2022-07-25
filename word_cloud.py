# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk

nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words('portuguese')

words = []

with open('db.txt', 'r', encoding='utf-8') as File:
    for line in File:
        if len(line) > 3:  # Dummy stopwords filter
            words.append(str(line))

wordcloud = WordCloud(
    width=400,
    height=400,
    stopwords=stopwords,
    background_color='black',
    min_font_size=10).generate(' '.join([item for item in words]))

# plot the WordCloud image
plt.figure(figsize=(24, 24), facecolor=None)
plt.imshow(wordcloud)
plt.axis("on")
plt.tight_layout(pad=0)
plt.show()

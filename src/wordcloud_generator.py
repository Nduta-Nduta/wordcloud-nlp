from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os
import nltk
from nltk.corpus import opinion_lexicon, stopwords
import string
from collections import Counter

# --- Ensure NLTK data is downloaded ---
nltk.download('opinion_lexicon')
nltk.download('stopwords')

# --- Path to reviews.txt ---
data_path = os.path.join(os.path.dirname(__file__), '../data/reviews.txt')

# Read the reviews
with open(data_path, 'r', encoding='utf-8') as file:
    text = file.read().lower()

if not text.strip():
    raise ValueError("The reviews.txt file is empty!")

# --- Clean text ---
text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
words = text.split()
words = [w for w in words if w not in stopwords.words('english')]  # remove stopwords

# --- Positive and negative words from NLTK ---
positive_words = set(opinion_lexicon.positive())
negative_words = set(opinion_lexicon.negative())

# --- Filter words ---
positive_text = " ".join([w for w in words if w in positive_words])
negative_text = " ".join([w for w in words if w in negative_words])

# --- Generate word clouds ---
wc_positive = WordCloud(
    width=800, height=400, background_color='white', stopwords=STOPWORDS
).generate(positive_text)

wc_negative = WordCloud(
    width=800, height=400, background_color='black', stopwords=STOPWORDS, colormap='Reds'
).generate(negative_text)

# --- Display ---
plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
plt.imshow(wc_positive, interpolation='bilinear')
plt.axis('off')
plt.title('Positive Words')

plt.subplot(1, 2, 2)
plt.imshow(wc_negative, interpolation='bilinear')
plt.axis('off')
plt.title('Negative Words')

plt.show()

# --- Top 10 word frequencies ---
pos_counts = Counter([w for w in words if w in positive_words])
neg_counts = Counter([w for w in words if w in negative_words])

print("Top 10 positive words:", pos_counts.most_common(10))
print("Top 10 negative words:", neg_counts.most_common(10))

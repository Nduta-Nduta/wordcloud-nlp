# src/app.py
import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import opinion_lexicon, stopwords
import string
from collections import Counter

# --- Download NLTK data ---
nltk.download('opinion_lexicon')
nltk.download('stopwords')

st.title("Interactive Sentiment Word Cloud")
st.write("Upload a text file of reviews to generate positive and negative word clouds.")

# --- File uploader ---
uploaded_file = st.file_uploader("Choose a text file", type="txt")

if uploaded_file is not None:
    # Read file
    text = uploaded_file.read().decode('utf-8').lower()
    
    if not text.strip():
        st.error("The uploaded file is empty!")
    else:
        # Clean text
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        words = [w for w in words if w not in stopwords.words('english')]

        # Positive/negative words
        positive_words = set(opinion_lexicon.positive())
        negative_words = set(opinion_lexicon.negative())

        positive_text = " ".join([w for w in words if w in positive_words])
        negative_text = " ".join([w for w in words if w in negative_words])

        # Generate word clouds
        wc_positive = WordCloud(width=800, height=400, background_color='white', stopwords=STOPWORDS).generate(positive_text)
        wc_negative = WordCloud(width=800, height=400, background_color='black', stopwords=STOPWORDS, colormap='Reds').generate(negative_text)

        # Display word clouds side by side
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        axes[0].imshow(wc_positive, interpolation='bilinear')
        axes[0].axis('off')
        axes[0].set_title("Positive Words")

        axes[1].imshow(wc_negative, interpolation='bilinear')
        axes[1].axis('off')
        axes[1].set_title("Negative Words")

        st.pyplot(fig)

        # Show top 10 words
        pos_counts = Counter([w for w in words if w in positive_words])
        neg_counts = Counter([w for w in words if w in negative_words])

        st.write("Top 10 Positive Words:", pos_counts.most_common(10))
        st.write("Top 10 Negative Words:", neg_counts.most_common(10))

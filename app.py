import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import nltk
import re
from nltk.corpus import stopwords
import collections
from nltk.corpus import wordnet
import pickle

# Load the classifier and TF-IDF vectorizer from the pickle files
with open("classifier.pickle", "rb") as f:
    clf = pickle.load(f)

with open("TfidfModel.pickle", "rb") as f:
    tfidf = pickle.load(f)

def getSentiment(text):
    # PREPROCESSING THE DATASET
    text = str(text)
    text = text.lower()
    text = re.sub(r"that's","that is",text)
    text = re.sub(r"there's","there is",text)
    text = re.sub(r"what's","what is",text)
    text = re.sub(r"where's","where is",text)
    text = re.sub(r"it's","it is",text)
    text = re.sub(r"who's","who is",text)
    text = re.sub(r"i'm","i am",text)
    text = re.sub(r"she's","she is",text)
    text = re.sub(r"he's","he is",text)
    text = re.sub(r"they're","they are",text)
    text = re.sub(r"who're","who are",text)
    text = re.sub(r"ain't","am not",text)
    text = re.sub(r"wouldn't","would not",text)
    text = re.sub(r"shouldn't","should not",text)
    text = re.sub(r"can't","can not",text)
    text = re.sub(r"couldn't","could not",text)
    text = re.sub(r"won't","will not",text)

    text = re.sub(r"\W"," ",text)
    text = re.sub(r"\d"," ",text)
    text = re.sub(r"\s+[a-z]\s+"," ",text)
    text = re.sub(r"^[a-z]\s+"," ",text)
    text = re.sub(r"\s+[a-z]$"," ",text)
    text = re.sub(r"\s+"," ",text)

    sent = clf.predict(tfidf.transform([text]).toarray())

    return sent[0]


def main():
    st.title("Review Sentiment Comparison")
    st.text("1.Monitoring reviews which have different review headline and review body")
    with st.container():
        review_headline = st.text_input("Enter the review headline:")
        review_body = st.text_area("Enter the review body:")

        if st.button("Compare Sentiments"):
            headline_sentiment = getSentiment(review_headline)
            body_sentiment = getSentiment(review_body)

            if headline_sentiment != body_sentiment:
                st.error("The review may be fake!")
            else:
                st.success("The review seems genuine!")
    
    
    
    st.text("2. Users which are posting either all positive or negative reviews on different products of same brand")
    
    with st.container():
        reviews = []

        for i in range(4):
            review = st.text_input(f"Enter Product {i+1} Review:", key=f"review_{i}")
            reviews.append(review)

        if st.button("Analyze Sentiments"):
            sentiments = [getSentiment(review) for review in reviews]
            if len(set(sentiments)) == 1:
                st.error("All reviews have the same sentiment. The reviews may be fake.")
            else:
                st.success("Reviews have different sentiments. They seem genuine.")


            
            
if __name__ == "__main__":
    main()

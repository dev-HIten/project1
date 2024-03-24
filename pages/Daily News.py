import streamlit as st
import requests

def news(url):
    r=requests.get(url)
    data = r.json()
    articles = data['articles']
    for article in articles:
        st.header(article["title"])
        try:
            st.image(article["urlToImage"])
        except:
            pass
        st.write(article["content"])
        st.caption(article["url"])


st.title("Whats happening in India")
news(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=f40834182cb742eead2ce3cd4998592a")

st.title("US News")
news("https://newsapi.org/v2/top-headlines?country=us&apiKey=f40834182cb742eead2ce3cd4998592a")

st.title("Business News")
news(f"https://newsapi.org/v2/top-headlines?category=business&apiKey=f40834182cb742eead2ce3cd4998592a")

st.title("Sports News")
news(f"https://newsapi.org/v2/top-headlines?category=sports&apiKey=f40834182cb742eead2ce3cd4998592a")

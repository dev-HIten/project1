import streamlit as st
import requests
# from api import movieApi
st.title('Movie Rating')

title=st.text_input('Enter the Movie or Web series name')
st.write()

if title:
    try:
        url=f"http://www.omdbapi.com/?t={title}&apikey=84c866db"
        r=requests.get(url).json()

        col1 , col2 = st.columns([1,2])
        
        with col1:
            st.image(r['Poster'])
            st.caption(f"Year: {r['Year']}")
            st.caption(f"Genre: {r['Genre']}")
            st.caption(f"Awards: {r['Awards']}")

        with col2:
            st.header(r["Title"])
            st.caption(f"Language {r['Language']}")
            st.write(f"Plot: {r['Plot']}")
            st.markdown(f"**Actors**: {r['Actors']}")
            st.markdown(f"**Directors**: {r['Director']}")
            st.markdown(f"**Writers**: {r['Writer']}")
            st.markdown(f"**Box Office Revenue** {r['BoxOffice']}")
            st.markdown(f"**IMDB Rating**: {r['imdbRating']}")
        st.progress(float(r['imdbRating'])/10)
    
        # st.write(r)
        
    except:
        st.error('No movie found , Please check the input')

import streamlit as st
from pytube import YouTube
import io

st.title("Youtube Video downloader")
st.caption("Longer video takes time to load,please be patience")

link = st.text_input("Enter the YouTube video URL: ",placeholder="paste here",value="https://www.youtube.com/watch?v=MvsAesQ-4zA")

if link:
    video = io.BytesIO()
    try:
        yt = YouTube(link)
        st.video(link)
        stream = yt.streams.get_highest_resolution()
        stream.stream_to_buffer(video)
        video=video.getvalue()
        col1 , col2 ,col3 = st.columns([1,1,1])
        with col2:
                st.download_button(label='Download Video', data=video, file_name='video.mp4', mime='video/mp4')
    except:
        st.warning("Please, Enter correct youtube link")        
    
            


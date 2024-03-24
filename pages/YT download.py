import streamlit as st
from pytube import YouTube
import io

st.title("Youtube Video downloader")
st.caption("Longer video takes time to load,please be patience")

link = st.text_input("Enter the YouTube video URL: ",placeholder="paste here",value="https://www.youtube.com/watch?v=tPEE9ZwTmy0&pp=ygUZc21hbGxlc3QgdmlkZW8gb24geW91dHViZQ%3D%3D")

if link:
    video = io.BytesIO()
    try:
        yt = YouTube(link)
        st.video(link)
        stream = yt.streams.get_highest_resolution()
        stream.stream_to_buffer(video)
        video=video.getvalue()
        col1 , col2 = st.columns([1,1])
        with col1:
                st.download_button(label='Download Video', data=video, file_name='video.mp4', mime='video/mp4')
        with col2:
              preview=st.button(label="Watch Preview")
        if preview:
              st.video(video)       
    except:
        st.warning("Please, Enter correct youtube link")        
    
            


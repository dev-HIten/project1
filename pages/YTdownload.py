import streamlit as st

from pytube import YouTube
import io
from PIL import Image

st.title("Youtube Video downloader")
st.caption("Longer video takes ,patience is key to success")

link = st.text_input("Enter the YouTube video URL: ",placeholder="paste here",value="https://www.youtube.com/watch?v=5DEdR5lqnDE")

if link:
    buffer = io.BytesIO()
    try:
        yt = YouTube(link)
        st.subheader(yt.title)
        thumbnail_url = yt.thumbnail_url
        st.image(thumbnail_url, caption=yt.title, use_column_width=True)

        stream = yt.streams.get_highest_resolution()
        stream.stream_to_buffer(buffer)
        col1 , col2 ,col3 = st.columns([1,1,1])
        with col1:
                st.download_button(label='Download Video', data=buffer.getvalue(), file_name='video.mp4', mime='video/mp4')
        with col2:
              st.link_button(label="Watch this video",url=link)
        with col3:
                st.download_button(label="Download Thumbnail", data=thumbnail_url, file_name="thumbnail.jpg",mime="image/jpg")

    except:
        st.warning("Please, Enter correct youtube link")        
    
            


import streamlit as st
from pytube import YouTube
import io

st.title("Youtube Video downloader")
st.caption("Longer video takes time to load,please be patience")

link = st.text_input("Enter the YouTube video URL: ",placeholder="paste here",value="https://www.youtube.com/watch?v=tPEE9ZwTmy0&pp=ygUZc21hbGxlc3QgdmlkZW8gb24geW91dHViZQ%3D%3D")

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
        video=buffer.getvalue()
        with col1:
                st.download_button(label='Download Video', data=video, file_name='video.mp4', mime='video/mp4')
        with col2:
              preview=st.button(label="Watch Preview")
        with col3:
                st.download_button(label="Download Thumbnail", data=thumbnail_url, file_name="thumbnail.jpg",mime="image/jpg")
        if preview:
              st.video(video)
       
    except:
        st.warning("Please, Enter correct youtube link")        
    
            


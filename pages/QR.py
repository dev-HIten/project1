import streamlit as st
import qrcode
import io

#qr code

image=io.BytesIO()
st.title('QR code generator')
q=st.text_input('Enter the data to make QR code')
img = qrcode.make(q)
img.save(image)
st.image(image, caption='Your personalised QR code')
btn = st.download_button(label="Download Image",data=image,file_name="qr.png",mime="image/png" )
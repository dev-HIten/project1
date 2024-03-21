import streamlit as st
import qrcode
import io

#qr code

image=io.BytesIO()
st.title('QR code generator')
q=st.text_input('Enter the data to make qr code')
img = qrcode.make(q)
type(img)  # qrcode.image.pil.PilImage
img.save(image)
st.image(image, caption='Your personalised qr code')
btn = st.download_button(
            label="Download image",
            data=image,
            file_name="qr.png",
            mime="image/png"
          )
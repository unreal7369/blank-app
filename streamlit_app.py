import streamlit as st
from PIL import Image

st.set_page_config(layout="centered", page_title="Love Me Valentine")
st.markdown("## ❤️ **Love Me Valentine**")

uploaded = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
if uploaded:
    st.image(Image.open(uploaded), width=200)
else:
    st.info("Upload any picture (it doesn't have to be named valentine.png)")

st.markdown("### Do you love me?")
col1, col2 = st.columns(2)
response = ""
if col1.button("No"):
    response = "😢 Oh... I’ll keep trying!"
if col2.button("Yes"):
    response = "🥰 I love you too!"
if response:
    st.success(response)

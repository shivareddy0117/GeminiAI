from dotenv import load_dotenv
from PIL import Image
load_dotenv()##loading all the env variables
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input, image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text


st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")
input = st.text_input("Input:", key="Input")
uploaded_file = st.file_uploader("choose image", type=["jpg","jpeg","png",])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image.", use_column_width=True)
submit = st.button("Tell me about the image")
##when submit is clicked
if submit:
    response = get_gemini_response(input,image)
    st.subheader("the response is")
    st.write(response)
from dotenv import load_dotenv

load_dotenv() # load all the environment variable from .env
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro vision 
model=genai.GenerativeModel('gemini-pro-vision')

def get_gimini_responce(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text



def input_image_data(uploaded_file):
    if uploaded_file is not None:
        # read files into bytes
        byte_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":byte_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("file not found")

st.set_page_config(page_title="MutliLanguage Invoice Extrater",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("MutliLanguage Invoice Extrater 🤖")
input=st.text_input("Input Prompt", key="input")
uploaded_file=st.file_uploader("Choees an Image of Invoice ...", type=["jpg","png","jpeg"])

image=""

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
submit=st.button("Tell me about invoice")


input_prompt="""
You are an expert in understanding invoices. we will upload a image invoice and you will have to answer 
any question based on the uploaded invoice image  
"""


if submit:
    image_data=input_image_data(uploaded_file)
    response = get_gimini_responce(input_prompt,[image],input)
    st.header("The Response is ")
    st.write(response)
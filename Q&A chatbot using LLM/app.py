# Q&A chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os

def get_openai_responce(question):
    llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="text-davinci-003",temperature=0.5)
    responce=llm(question)
    return responce

st.set_page_config(page_title="Q&A Demo")

st.header("Q&A Chatbot Application")
input=st.text_input("input: ", key="input")
response=get_openai_responce(input)
submit=st.button("Ask the question")

if submit:
    st.subheader("The Response is")
    st.write(response)
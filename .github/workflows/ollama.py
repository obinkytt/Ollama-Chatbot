from langchain_community.llms import Ollama

import streamlit as st

llm = Ollama (model = "llama3.2")

st.title("Chatbot using Llama3")

prompt = st.text_area("Enter your prompt:")

if st.button("genetrate"):

    if prompt:
        with st.spinner("Generateing response .."):
            st.write(llm.invoke(prompt, stop=['<|eot_id|>']))

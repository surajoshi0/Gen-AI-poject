from google import genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

st.title("Prompt Bot ")

SYSTEM_PROMPT = "You are a helpful assistant. Please respond to the user queries."
USER_TEMPLATE = "Question: {question}"

input_text = st.text_input("Search the topic you want")

if input_text:
    full_prompt = f"{SYSTEM_PROMPT}\n\n{USER_TEMPLATE.format(question=input_text)}"

    try:
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = full_prompt
        )
        st.write(response.text)
    except Exception as e:
        st.error(f"Error calling Gemini API: {e}")
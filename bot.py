import os

from groq import Groq
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


st.title("AI Assistent using python")
prompt =st.text_input("enter your prompt")

if st.button("submit"):
  client = Groq( api_key=os.environ.get("GROQ_API_KEY"))

  chat_completion = client.chat.completions.create(messages=[ {"role": "user","content": prompt,  }],model="llama3-8b-8192")

  st.write(chat_completion.choices[0].message.content)
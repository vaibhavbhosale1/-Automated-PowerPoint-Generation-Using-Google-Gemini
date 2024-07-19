from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')

# Function for getting response from the Gemini Model
def gemini_res(question: str) -> str:
    response = model.generate_content(question)
    return response.text

# Streamlit App configuration
st.set_page_config(page_title='Chatbot Using Gemini Pro By Vaibhav')

st.header('Google Gemini Application by Vaibhav')

# Input field
user_input = st.text_input('Input:', key='input')

# Submit button
submit = st.button('Send your Question and get Answer')

# When submit button is clicked
if submit:
    responses = gemini_res(user_input)
    st.subheader('Your Answer is')
    st.write(responses)
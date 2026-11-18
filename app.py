import streamlit as st
from groq import Groq
st.set_page_config(page_title = 'Placement Practice' , layout='centered')
st.title("AI Interview Assistant")
st.caption("Practice and Prepare for your Placement")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API key is missing. Add it in Advanced settings")
  st.stop()
role = st.selectbox('Job Title', ['Machine Learning Engineer', 'Senior Software', 'Data Analyst', 'Prompt Engineer', 'DevOps Engineer', 'Others'])
if role == "Others":
  st.text_input("Enter your Job Title", "XXXXXX")
model = st.selectbox('Model', ['qwen/qwen3.8-27b','openai/gpt-oss-120b'])
model = st.selectbox('Difficulty',['Beginner','Intermediate','Advanced'])
model = st.radio('Activity',['Generate Questions','Generate Code Questions','Evaluate Answer','Improve Answer'])
if mode == 'Generate Questions':
    count = st.slider("Number of Questions",1,10,5)
  elif mode == 'Generate Code Question':
    topic = st.selectbox('Topics', ['SQL','AIML','Python','DSA','C++/C','JAVA','ADA'])
    count = st.slider("Number of Questions",1,10,5)

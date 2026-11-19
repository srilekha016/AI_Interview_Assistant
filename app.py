import streamlit as st
from groq import Groq
st.set_page_config(page_title = "Placement Practice", page_icon = '💞', layout="centered")
st.title('AI Placement Assistent')
st.caption("Practice and prepare for your Placements here")
st.caption("Launched by BV Srilekha")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API Key is missing. Add it in Advanced settings")
  st.stop()
role = st.selectbox('Job Title',['Machine Learning Engineer','Senior software engineer','Prompt Engineering','Data Analyst','Devop Engineer','other'])
if role == "other":
  st.text_input("Enter your Job Title","XXXXXXX")
gen_model = st.selectbox("Model",['qwen/qwen3.8-27b','openai/gpt-oss-20b'])
level = st.selectbox("Level",['Beginner','Intermediate','Advance'])
mode = st.radio('Activity',['Generate Questions','Generate Code Questions','Evaluate Answer','Improve Answer'])
if mode == 'Generate Questions':
   count = st.slider("Number of Questions",1,10,5)
elif mode == 'Generate Code Questions':
   topic = st.selectbox("topic",['SQL','AIML','Python','DSA','C++/C','JAVA','ADA','DBMS'])
   count = st.slider("Number of Questions",1,10,5)
else:
  question = st.text_area('Enter Interview Quesion here')
  answer = st.text_area('Enter your answer', height =160)
if st.button("Generate AI Responce", type = "primary"):
  if mode in ['Evaluate Answer', 'Improve Answer'] and (not question.strip() or not answer.strip()):
    st.warning("Please enter a valid Question and Answer")
    st.stop()
  topic = "Topics is" + topic + "Difficulty is" + level
if mode == "Generate Questions":
  task = "Generate " + str(count) + "Frequently asked Interview Questions 3 theory and 2 conceptual .Do not give answer give hint"
elif mode == "Generate Code Questions":
  task = "Generate " + str(count) + "Frequently asked coding questions on topic " + topic + "and give hints to solve them also add be accuarate "
elif mode == "Evaluate Answer":
  task = "Questions : " + question + "My Answer :" + answer + "Evaluate this answer based on concepts , relevence , communication length of amswer.Give each rating out of 5"
elif mode == "Improve Answer":
  task = "Questions : " + question + "My Answer :" +answer + "Improve the answer based on coding , communicatoin ,aplitute,preparation interview"
background = "Job role : " +role+ " Difficulti level "+level
with st.spinner("Generating your answer ..."):
  try:
    responce = client.chat.completions.create(
        model = gen_model,
      messages = [{"role": "system",
                  "content":"Act as a Senior Interviewer both HR and Technical expert"},
                  {"role" : "user",
                  "content" : background + task }],
      temperature = 0.7,
      max_tokens = 1800 )
    output = responce.choices[0].message.content
    st.subheader("AI Responce")
    st.markdown(output)
    st.download_button("Download Responce", output,file_name = "Interview_Assistant.txt", mime ='text/plain')
  except Exception as e:
    st.error ("API connection was unsuccessful :", e)
    st.info ("Please check your API key and rate limits")
st.caption("Powered by Streamlit.io and GitHub. Using LLM API")
    


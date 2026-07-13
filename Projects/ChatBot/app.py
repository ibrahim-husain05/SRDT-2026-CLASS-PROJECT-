import streamlit as st 
from coordinator import decide_agent
from memory import add_memory

st.title("Multi-Agent AI Chatbox")

if "messages" not in st.session_state:
  st.session_state.messages=[]
  
for msg in st.session_state.messages:
  st.chat_message(msg["role"]).write(msg["content"])

prompt=st.chat_input("Ask something") 

if prompt:
  add_memory(st.session_state.messages,"user",prompt)
  
  st.chat_message("user").write(prompt)     
  
  response = decide_agent(st.session_state.messages,prompt)
  
  add_memory(st.session_state.messages,"assistant",response)
  
  st.chat_message("assistant").write(response)
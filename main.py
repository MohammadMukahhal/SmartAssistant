import streamlit as st
from support import CleanQuestion
from NLP import processNLP
from Query_wikipedia import WikiQuery

with st.sidebar:
    #st.markdown("[(https://www.flaticon.com/free-icons/artificial-intelligence)]")
    st.markdown("Welcome to the smart teaching assistant! This site could answer your questions using the BERT model and wikipedia data!")

st.title("💬 Smart Teaching Assistant") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi, do you have any questions I can answer for you?"}]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    #Process the prompt using BERT
    searchQuery = CleanQuestion(prompt)
    # context = "Bill Gates is the richest man in the world"
    context = WikiQuery(searchQuery)
    print("CONTEXT: " + context)
    print(context)
    #Process the prompt using BERT
    response = processNLP(prompt,context)

    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
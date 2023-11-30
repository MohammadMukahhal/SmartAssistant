import streamlit as st
from support import CleanQuestion
from NLP import processNLP


with st.sidebar:
    #st.markdown("[(https://www.flaticon.com/free-icons/artificial-intelligence)]")
    st.markdown("Placeholder")

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
    context = "In recent years, deep learning has gained immense popularity in the field of artificial intelligence. One of the pivotal developments in this domain was the introduction of transformer-based models like BERT (Bidirectional Encoder Representations from Transformers). These models have demonstrated exceptional performance across various natural language processing tasks, including text classification, named entity recognition, question answering, and more."
    #Process the prompt using BERT
    response = processNLP(prompt,context)

    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)


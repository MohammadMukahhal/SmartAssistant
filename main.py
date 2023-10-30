import streamlit as st


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
    response = "Placeholder for bert response"
    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)


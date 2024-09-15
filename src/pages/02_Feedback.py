import streamlit as st
from assistant import Model

model = Model()

st.title("Feedback bot")

st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if st.session_state['thread_id']:
        model.send_message(prompt, st.session_state['thread_id'])
    else:
        thread = model.create_thread(prompt)
        st.session_state['thread_id'] = thread.id

    messages = model.get_messages(
        st.session_state['thread_id'], st.session_state.assistants["Feedbackbot"])
    response = messages[0]

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})

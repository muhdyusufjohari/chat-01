import streamlit as st
import groq
import os

# Initialize Groq client
if 'GROQ_API_KEY' in st.secrets:
    client = groq.Groq(api_key=st.secrets['GROQ_API_KEY'])
elif 'GROQ_API_KEY' in os.environ:
    client = groq.Groq(api_key=os.environ['GROQ_API_KEY'])
else:
    st.error("Groq API key not found. Please set it in Streamlit secrets or as an environment variable.")
    st.stop()

# Streamlit app
st.title("Chatbot using Groq API")

# Model selection
model = st.selectbox("Choose a model:", ["llama-3.1-8b-instant", "mixtral-8x7b-32768"])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What is your question?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            model=model,
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Clear chat history
if st.button("Clear Chat History"):
    st.session_state.messages = []
    st.experimental_rerun()

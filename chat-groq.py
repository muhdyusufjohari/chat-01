import streamlit as st
import requests

st.title("Groq LLM Chatbot")

user_input = st.text_input("You:", "")

def get_groq_response(user_message):
    api_key = st.secrets["general"]["groq_api_key"]  # Accessing the API key from secrets
    url = "https://api.groq.com/v1/chat"  # Example endpoint
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "message": user_message
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("response", "Sorry, I didn't get that.")

if user_input:
    response = get_groq_response(user_input)
    st.text_area("Bot:", value=response, height=200)

import streamlit as st
import requests

# Set the title of the app
st.title("Groq LLM Chatbot")

# Input field for user messages
user_input = st.text_input("You:", "")

# Function to call the Groq API
def get_groq_response(user_message):
    api_key = "YOUR_GROQ_API_KEY"  # Replace with your actual Groq API key
    url = "https://api.groq.com/v1/chat"  # Example endpoint, check Groq documentation for the correct one
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "message": user_message
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("response", "Sorry, I didn't get that.")

# Display the chatbot's response
if user_input:
    response = get_groq_response(user_input)
    st.text_area("Bot:", value=response, height=200)

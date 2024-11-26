import streamlit as st
import aisuite as ai
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = "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"

client = ai.Client()

def get_ai_response(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful agent."},
        {"role": "user", "content": prompt}
    ]
    
    try:
        response = client.chat.completions.create(
            model="groq:llama-3.2-3b-preview",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

st.title("🤖 Tejash Chatbot")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat history in ChatGPT-style
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box for user
if prompt := st.chat_input("Type your message..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ai_response(prompt)
            st.markdown(response)
    
    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Function to ask question and get response
def ask_question():
    input_text = st.text_input("You:", key="input")
    if st.button("Ask"):
        if input_text:
            # Add user query to session state chat history
            st.session_state['chat_history'].append(("You", input_text))
            # Get response from the model
            response = get_gemini_response(input_text)
            st.subheader("Response:")
            for chunk in response:
                st.write(chunk.text)
                # Add model response to session state chat history
                st.session_state['chat_history'].append(("Gemini", chunk.text))
        else:
            st.warning("Please enter your question.")

# Display the chat history
def display_chat_history():
    st.subheader("Chat History:")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")

# Teacher-like responses based on common questions
def teacher_response(question):
    if "how to" in question.lower() or "explain" in question.lower():
        return "Sure, let me explain that to you. [Insert detailed explanation here]."
    elif "solve" in question.lower() or "calculate" in question.lower():
        return "To solve this, you need to follow these steps: [Insert step-by-step solution]."
    else:
        return get_gemini_response(question)

# UI
st.set_page_config(page_title="Student Q&A Chatbot")

st.header("Student Q&A Chatbot (Teacher Mode)")

ask_question()
display_chat_history()
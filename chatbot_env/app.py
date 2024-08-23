import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Set the Google API key directly (not recommended for production)
os.environ["GOOGLE_API_KEY"] = "AIzaSyCtYlRd0sXsfSMFfjYrx7KJGVeKUVjbOWo"

# Initialize the ChatGoogleGenerativeAI model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=200,
    timeout=None,
    max_retries=2,
)

def get_ai_response(user_question):
    messages = [
        (
            "system",
            "You are a helpful assistant that provides information in a clear and structured format. For instance, if asked about popular programming languages, list them with headings and bullet points.",
        ),
        ("human", user_question),
    ]
    ai_response = llm.invoke(messages)
    return ai_response.content

# Initialize session state
if 'question' not in st.session_state:
    st.session_state.question = ""

if 'answer' not in st.session_state:
    st.session_state.answer = ""

def submit_question():
    # Update the question and get the response
    st.session_state.question = st.session_state.user_input
    if st.session_state.question:
        st.session_state.answer = get_ai_response(st.session_state.question)
    st.session_state.user_input = ""  # Clear the input field after submission

# Streamlit user interface
st.title("HM AI")

# Input text box for user question
user_input = st.text_input("Ask me anything:", key="user_input", on_change=submit_question)

# Display the answer if available
if st.session_state.answer:
    st.write(f"Answer: {st.session_state.answer}")

# Hide the question input after submission
if st.session_state.question:
    st.write(f"Question: {st.session_state.question}")

# Optionally, provide a button to reset the question and answer if needed
if st.button('Reset'):
    st.session_state.question = ""
    st.session_state.answer = ""

import streamlit as st
import datetime
import requests
import sys

BASE_URL = "http://localhost:8000"



st.set_page_config(
    page_title="🌍 Travel Planner Agentic Application",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.title("🌍 Travel Planner Agentic Application")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("How can I help you in planning a trip? Let me know where do you want to visit.")

with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("Enter your travel query:")
    submit_button = st.form_submit_button(label="Submit")

if submit_button and user_input.strip():
    try:
        with st.spinner("Planning your trip..."):
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)
            
        if response.status_code == 200:
            answer = response.json().get("answer", "Sorry, I couldn't get an answer.")
            markdown_content = f"""# 🌍 AI Travel Plan

            # **Generated:** {datetime.datetime.now().strftime('%Y-%m-%d at %H:%M')}  
            ## **Your Query:**
            {user_input}
            ## **Travel Plan:**
            {answer}
            """
            st.markdown(markdown_content)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        raise f"An error occurred: {str(e)}"
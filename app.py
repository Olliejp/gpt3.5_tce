import streamlit as st
import pandas as pd
import openai

openai.api_key = st.secrets["APIKEY"]

def openai_call(text):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a professional writing assistant who helps writers produce high quality content"},
            {"role": "user", "content": text}
        ]
    )
    return response

def check_password():
    def password_entered():
        """Check whether correct password entered by user"""
        if st.session_state["password"] == st.secrets["PASSWORD"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        return True
        

if check_password():
    st.title("TCE GPT3.5 demo app")

    input_text = st.text_area("Please enter your prompt")

    if st.button("Let's go!!"):
        data_load_state = st.text("BEEEP BOOP BEEEEP BOOOOOPP")
        response = openai_call(input_text)
        data_load_state.text("")
        st.write(response['choices'][0]['message']['content'])


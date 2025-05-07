import streamlit as st

# Title and header
st.title("Hello, Streamlit!")
st.header("🎯 Objective: Understand basic components")

# Input fields
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120)

# Display user input
if name:
    st.write(f"👋 Hello, {name}!")
if age:
    st.write(f"🎂 You are {int(age)} years old.")

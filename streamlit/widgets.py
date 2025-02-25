import streamlit as st
import pandas as pd
from password_checker import feedback

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}")

age = st.slider("How old are you?", 0, 130, 25)
if age:
    st.write(f"I am {age} years old")

options = ["Python", "Java", "C++", "Go", "Rust", "JavaScript"]
choice = st.selectbox("What is your favorite programming language?", options)
if choice:
    st.write(f"Your favorite programming language is {choice}")

colors = ["red", "green", "blue", "yellow", "purple", "orange"]
color = st.radio("What is your favorite color?", colors)
if color:
    st.write(f"Your favorite color is {color}")

fruits = ["Apple", "Banana", "Orange", "Grape", "Watermelon", "Mango"]
fruit = st.multiselect("What is your favorite fruit?", fruits)
if fruit:
    st.write(f"Your favorite fruit is {' '.join(fruit)}")

birthday = st.date_input("What is your birthday?")
if birthday:
    st.write(f"Your birthday is {birthday}")

time = st.time_input("What time is it now?")
if time:
    st.write(f"It is {time}")

file = st.file_uploader("Upload a file", type="csv")
if file is not None:
    st.write(f"You have uploaded a file named {file.name}")
    df = pd.read_csv(file)
    st.write(df)
    st.line_chart(df)

multi_file = st.file_uploader("Upload multiple files", accept_multiple_files=True, type=["jpg", "png", "jpeg", "gif"])
if multi_file is not None: 
    for file in multi_file:
        st.write(f"You have uploaded a file named {file.name}")
        st.image(file)

number = st.number_input("Enter a number", 0.0, 100.0, 50.0)
st.write(f"You have entered the number {number}")

agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("You have agreed to the terms and conditions")

text = st.text_area("Enter some text")
if text:
    st.write(f"You have entered the text: {text}")

password = st.text_input("Enter your password", type="password")
if password:
    fb = feedback(password)
    st.write(fb)

data = {
    "Name": ["Ali", "Budi", "Ciera", "Doni"],
    "Age": [25, 30, 35, 41],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
st.write("Display the dataframe")
st.write(df)


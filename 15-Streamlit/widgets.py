import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:") ## Show a text-box
st.write(f"Your name is {name}.")

age=st.slider("Select your age:",0,100,25) ## Create a slider whose default set to 25 and ranging between 0 to 100

st.write(f"Your age is {age}.")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options) ## Show a drop-box having options
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")

## data as dictionary
data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data) ## DataFrame = table (rows and columns)
df.to_csv("sampledata.csv") ## Saves the DataFrame df into a CSV file
st.write(df)


uploaded_file=st.file_uploader("Choose a CSV file",type="csv") ## upload file 

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)


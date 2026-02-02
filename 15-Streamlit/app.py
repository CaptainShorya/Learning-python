import streamlit as st
import pandas as pd
import numpy as np

## How to execute -> streamlit run file_name.py

## Title of the aplication
st.title("Hello Streamlit")

## Diplay a Simple Text
st.write("This is a simple text")

##create a simple Dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


## Display the Dataframe
st.write("Here is the dataframe")
st.write(df)


##create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c'] ## generate random number from a normal distribution(mean=0,std deviation=1)
    ## 20 = rows, 3 = columns , generate 20 × 3 random numbers
)
st.line_chart(chart_data)
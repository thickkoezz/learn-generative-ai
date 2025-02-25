import streamlit as st
import pandas as pd
import numpy as np

st.title("Selamat Belajar")

st.write("Ini teks sederhana")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
    'third column': [100, 200, 300, 400]
})

## display the dataframe
st.write("Contoh tampilan dataframe")
st.write(df)

## create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)


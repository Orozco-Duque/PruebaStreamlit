import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Simple Data Dashboard')

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])   

if upload_file is not None:
    #st.write("File uploaded successfully!")
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Description")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select columns to filter", columns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox("Select a value to filter", unique_values)
    filtered_data = df[df[selected_columns] == selected_value]
    st.write("Filtered Data")
    st.write(filtered_data)

    st.subheader("Data Visualization")
    selected_x = st.selectbox("Select X-axis column", columns)
    selected_y = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate Scatter Plot"):
        st.line_chart(filtered_data.set_index(selected_x)[selected_y])
else:
    st.write("Waiting for user input...")
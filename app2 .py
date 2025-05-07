import streamlit as st
import pandas as pd

# Title
st.title("Load and Display Data")

# File uploader widget to upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# If file is uploaded, load and display data
if uploaded_file is not None:
    # Load the CSV file using pandas
    df = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.write("### Dataframe Preview")
    st.dataframe(df)

    # Checkbox to toggle viewing raw data
    if st.checkbox("Show raw data"):
        st.write(df)

    # Selectbox to filter data by a specific column
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter by", columns)

    # Display unique values of the selected column
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox(f"Select a value from {selected_column}", unique_values)

    # Filter the data based on the selected value
    filtered_df = df[df[selected_column] == selected_value]

    # Show the filtered data
    st.write(f"### Filtered Data by {selected_column} = {selected_value}")
    st.dataframe(filtered_df)

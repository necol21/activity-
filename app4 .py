import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import requests

# Title
st.title("COVID-19 Stats Visualization")

# Sidebar Input
st.sidebar.header("Filter Options")
country = st.sidebar.text_input("Enter country name", "United States")

# Load data from Our World In Data (OWID)
@st.cache_data
def load_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    try:
        df = pd.read_csv(url, parse_dates=["date"])
        return df
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return None

data = load_data()

# Filter and display
if data is not None:
    df_country = data[data['location'].str.lower() == country.lower()]
    
    if not df_country.empty:
        df_country.set_index('date', inplace=True)
        st.write(f"COVID-19 Data for {country}:", df_country[['total_cases', 'new_cases']].tail())

        # Plot confirmed cases over time
        st.subheader("Confirmed COVID-19 Cases Over Time")
        st.line_chart(df_country['total_cases'])

        st.subheader("Daily New Cases")
        st.bar_chart(df_country['new_cases'])

        st.subheader("Plotly Line Chart")
        fig = px.line(df_country, x=df_country.index, y='total_cases', title=f"Total Cases Over Time in {country}")
        st.plotly_chart(fig)

        st.subheader("Seaborn Heatmap: New Cases")
        heatmap_data = df_country[['new_cases']].resample('M').sum()
        fig = plt.figure(figsize=(10, 4))
        sns.heatmap(heatmap_data.T, annot=True, fmt=".0f", cmap="YlOrRd", cbar=True)
        st.pyplot(fig)
    else:
        st.warning("No data found for the specified country. Please check the name and try again.")
else:
    st.stop()

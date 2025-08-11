import streamlit as st
from fetch_data import get_weather_data

st.set_page_config(page_title="🌤 Weather App", layout="centered")

st.title("🌤 Weather Dashboard")
st.write("Enter a city name to get real-time weather data from OpenWeather.")

city = st.text_input("City Name", value="Dumka")

if st.button("Get Weather"):
    df, error = get_weather_data(city)
    if error:
        st.error(error)
    else:
        st.dataframe(df)
        st.success(f"Weather data for {city} loaded successfully!")
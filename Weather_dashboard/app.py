import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


API_KEY = "1a346bd29e6e2bc30b511bbaf33b3513"  
CITY = "New Delhi"  
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch Weather Data
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    weather_data = []
    for entry in data['list']:
        weather_data.append({
            "datetime": entry["dt_txt"],
            "temperature": entry["main"]["temp"],
            "humidity": entry["main"]["humidity"],
            "weather": entry["weather"][0]["description"]
        })
    df = pd.DataFrame(weather_data)
    df["datetime"] = pd.to_datetime(df["datetime"])
else:
    st.error("Error fetching weather data. Please check your API key or city name.")
    st.stop()


st.title("Weather Analysis Dashboard Fetching by Ayush")
st.subheader(f"City: {CITY}")

st.write("## Raw Weather Data")
st.dataframe(df)

st.write("## Temperature Trend")
st.line_chart(df.set_index("datetime")["temperature"])

st.write("## Humidity Trend")
st.line_chart(df.set_index("datetime")["humidity"])

st.write("## Weather Description Count")
st.bar_chart(df["weather"].value_counts())
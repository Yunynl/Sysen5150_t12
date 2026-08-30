import streamlit as st
import requests

st.title("SYSEN 5151 Lab 0")

response = requests.get("http://127.0.0.1:8000")

st.write(response.json()["message"])
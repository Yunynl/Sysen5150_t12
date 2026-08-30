import streamlit as st
import requests

st.title("SYSEN 5151 Lab 0")
st.markdown("**Team 12 - Team Members:** Zihan Li, Wentao Yu, Bochen Jiang, Yuhao Jiang")

response = requests.get("http://127.0.0.1:8000")

st.write(response.json()["message"])
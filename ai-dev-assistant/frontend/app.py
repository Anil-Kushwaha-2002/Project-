import streamlit as st
import requests

st.title("AI Developer Assistant")

question = st.text_area("Ask about your codebase")

if st.button("Ask AI"):

    res = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"question": question}
    )

    answer = res.json()["answer"]

    st.write(answer)
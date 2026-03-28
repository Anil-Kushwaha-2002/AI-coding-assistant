import streamlit as st
import requests

st.title("AI Coding Assistant")

prompt = st.text_area("Enter coding prompt", height=200)

if st.button("Generate Code"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt")

    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/generate",
                json={"prompt": prompt},
                timeout=60
            )

            if response.status_code == 200:

                data = response.json()

                st.subheader("Generated Code")
                st.code(data["result"], language="python")

            else:
                st.error("Backend error: " + response.text)

        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
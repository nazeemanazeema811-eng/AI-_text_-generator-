import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI Text Generator",
    page_icon="🤖"
)

st.title("🤖 AI Text Generator")
st.write("Generate text using Generative AI")

api_key = st.text_input(
    "Enter your API Key",
    type="password"
)

prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: Write a short paragraph about Artificial Intelligence"
)

if st.button("✨ Generate Text"):

    if not api_key:
        st.warning("Please enter your API key.")

    elif not prompt:
        st.warning("Please enter a prompt.")

    else:
        try:
            client = OpenAI(api_key=api_key)

            response = client.responses.create(
                model="gpt-5-mini",
                input=prompt
            )

            st.subheader("Generated Text")
            st.write(response.output_text)

        except Exception:
            st.error("Something went wrong. Please check your API key and try again.")

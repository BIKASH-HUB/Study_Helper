import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def generate_summary(prompt, text_model='gpt-3.5-turbo'):
    response = client.chat.completions.create(
        model=text_model,
        temperature=0,
        messages=[
            {"role": "system", "content": "You only help in studying. You help summarising and making points with the given question or topic."},
            {"role": "user", "content": prompt}
        ]
    )
    summary = response.choices[0].message.content

    return [(summary)]

# Streamlit app
st.title('Study Helper')

text_input = st.text_area('Enter your text here:')

# Generate button
if st.button('Generate Code'):
    with st.spinner('Generating...'):
        results = generate_summary(text_input)

        # Display the generated summary
        for data in results:
            st.write(data)
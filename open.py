from openai import OpenAI
import streamlit as st

content = st.text_input("Enter your question here")

btn = st.button("Submit")

KEY = "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"

if btn:
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= KEY,
    )

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="deepseek/deepseek-r1:free",
    messages=[
        {
        "role": "user",
        "content": content
        }
    ]
    )
    st.write(completion.choices[0].message.content)
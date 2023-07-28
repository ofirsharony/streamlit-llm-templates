import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage
)

# instructions
# Store your OpenAI key in env var OPENAI_API_KEY
# pip install openai langchain streamlit
# streamlit run single-question-llm.py

PROMPT = '''You are a professional storyteller. You will come up with entertaining stories that are engaging, imaginative, and captivating for the audience. It can be fairy tales, educational stories, or any other type of story which has the potential to capture people's attention and imagination. Depending on the target audience, you may choose specific themes or topics for your storytelling session e.g., if it’s children then you can talk about animals; If it’s adults then history-based tales might engage them better, etc.
---
Story title: {} Main character: {} Target audience: {}'''

openai_api_key = os.environ.get('OPENAI_API_KEY')
st.set_page_config(layout="centered", page_title="LLM stories generator")
st.markdown("## LLM Stories Generator")
st.markdown("### Personalized stories for the masses")

def generate_response(input_text, model_name):
    chat = ChatOpenAI(temperature=0.3, openai_api_key=openai_api_key, model_name=model_name)
    messages = [
        SystemMessage(content=input_text),
        # HumanMessage(content="Hi AI, how are you today?"),
        # AIMessage(content="I'm great thank you. How can I help you?"),
        # HumanMessage(content="I'd like to understand string theory.")
    ]

    return chat(messages)


with st.form('my_form'):
    open_ai_model = st.selectbox('Which OpenAI model should we use?', ('gpt-3.5-turbo-16k', 'gpt-4', 'gpt-3.5-turbo'))
    story_title = st.text_input("Story title", value="The author and the wonder")
    main_character = st.text_input("Main character", value="Mia, an inspiring author, searching meaning and purpose through a life full of grit and perseverance")
    target_audience = st.selectbox("Target audience",  ('Children', 'Students', 'Adults'))
    prompt = st.text_area('Prompt:', value=PROMPT, height=220)
    submitted = st.form_submit_button('Generate')

    if submitted:
        with st.spinner('Generating LLM response...'):
            narrative = generate_response(prompt.format(story_title, main_character, target_audience), open_ai_model)
            st.info(narrative.content)

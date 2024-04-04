from openai import OpenAI
import streamlit as st
import dotenv
import os
dotenv.load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
    # st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    # "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    # "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    # "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chat")
st.caption("🚀 Chatbot simples!")
st.text("")

model_options = ["","Gpt 4 Turbo ($0,004)", "Gpt 3.5 Turbo ($0.002)"]
models = {
    "Gpt 4 Turbo ($0,004)": "gpt-4-1106-preview",
    "Gpt 3.5 Turbo ($0.002)": "gpt-3.5-turbo-0125"
}
selected_model = st.selectbox("Escolha um modelo", model_options)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not selected_model or selected_model == '' or selected_model not in models.keys():
        st.info("Escolha um modelo para continuar.")
        st.stop()
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model=models[selected_model], messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

import openai
import streamlit as st
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Set the OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Model options
model_options = ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"]
model_choice = st.sidebar.selectbox("Select OpenAI Model:", model_options)

# LangChain configuration
llm = ChatOpenAI(temperature=0.9, model_name=model_choice, openai_api_key=openai.api_key)
prompt_template = ChatPromptTemplate.from_template("User: {user_input}\nAI:")
chain = LLMChain(llm=llm, prompt=prompt_template)

# Build Streamlit UI
st.title("Simple Chat Bot")

# Maintain chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Get user input
user_input = st.text_input("Input:", key="input_text")

# Add Send button and reset input
if st.button("Send"):
    if user_input:
        # Generate response using LangChain
        response = chain.run(user_input)
        
        # Add user input and response to chat history
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Bot: {response}")

# Display chat history
st.write("Chat History:")
for message in st.session_state.chat_history:
    st.write(message)

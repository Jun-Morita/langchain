import openai
import streamlit as st
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
import tempfile

# Set the OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Model options
model_options = ["gpt-4o", "gpt-4o-mini"]
model_choice = st.sidebar.selectbox("Select OpenAI Model:", model_options)

# LangChain configuration
llm = ChatOpenAI(temperature=0.9, model_name=model_choice, openai_api_key=openai.api_key)
prompt_template = ChatPromptTemplate.from_template("User: {user_input}\nAI:")
chain = LLMChain(llm=llm, prompt=prompt_template)

# Function to process PDF and create retriever
def process_pdf(pdf_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(pdf_file.read())
        tmp_file_path = tmp_file.name
    
    loader = PyPDFLoader(tmp_file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    
    embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)
    vectorstore = FAISS.from_texts([text.page_content for text in texts], embedding=embeddings)
    return vectorstore

# Build Streamlit UI
st.title("RAG Chat Bot")

# PDF upload
uploaded_pdf = st.file_uploader("Upload a PDF", type=["pdf"])
vectorstore = None
if uploaded_pdf is not None:
    vectorstore = process_pdf(uploaded_pdf)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Maintain chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Get user input
user_input = st.text_input("Input:", key="input_text")

# Add Send button and reset input
if st.button("Send"):
    if user_input:

        if retriever:
            retrieved_docs = retriever.get_relevant_documents(user_input)
            context = "\n".join([doc.page_content for doc in retrieved_docs])
            user_input_with_context = f"Context: {context}\nUser: {user_input}\nAI:"
            response = chain.run(user_input_with_context)
        else:
            response = chain.run(user_input)
        
        # Add user input and response to chat history
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Bot: {response}")

# Display chat history
st.write("Chat History:")
for message in st.session_state.chat_history:
    st.write(message)

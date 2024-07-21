# langchain

Sample Code for ChatGPT/LangChain Web Applications

This GitHub repository contains sample code for building web applications using ChatGPT and LangChain. It includes implementations for a simple chat bot and a Retrieval-Augmented Generation (RAG) chat bot.

## Environment Setup

First, create a Python environment:

> conda create -n langchain python=3.11
> conda activate langchain  

> pip install openai==1.35.13  
> pip install langchain==0.2.7  
> pip install langchain-community==0.2.7  
> pip install langchain-openai==0.1.17  
> pip install streamlit==1.36.0  
> pip install pypdf==4.3.0  
> pip install tiktoken==0.7.0  
> pip install faiss-cpu==1.8.0  

## OpenAI API Key

Create a secrets.toml file in the .streamlit folder and add the following code:

> OPENAI_API_KEY = "xxxxxxxx"  

Replace xxxxxxxx with your actual OpenAI API key.

## Execution

**Simple Chat Bot**

To run the simple chat bot:

> conda activate langchain    
> streamlit run chatbot.py  

**RAG Chat Bot**

To run the RAG chat bot:

> conda activate langchain    
> streamlit run chatbot_rag.py  

## Data

The data folder contains sample data used for the RAG Chat Bot. Make sure to place your PDF files or other relevant documents in this folder to enable the retrieval-augmented generation functionality.

## Reference

- [LangChain GitHub Repository](https://github.com/langchain-ai/langchain)
- [サクッと始めるプロンプトエンジニアリング【LangChain / ChatGPT】](https://zenn.dev/umi_mori/books/prompt-engineer)
